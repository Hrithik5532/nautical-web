from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from .models import  *
from taggit.models import Tag
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.contrib import messages #import messages
# Create your views here.

def home(request):
    banner_img = Banner.objects.all()[::-1]
    services = Services.objects.all()
    articles = Articles.objects.order_by('-id')[0:3]
    return render(request,"html/index.html",{'title':'Home','banner_img':banner_img,'services':services,'articles':articles})

def services(request):
    return render(request,'html/services.html',{'title':'Services'})

def contact_us(request):
    if  request.method =='POST':
        name = request.POST.get('name',None)
        email = request.POST.get('email',None)
        mobile = request.POST.get('mobile',None)
        company = request.POST.get('company',None)
        message = request.POST.get('message')

        print(name,email,mobile)
        if name== None or  email == None or mobile == None:
            messages.error(request,"Please Fill Correct Information !!!" )
            return redirect('contact_us')
        
        ContactEnquires.objects.create(name=name,message=message,email=email,mobile_number=mobile,company_name=company).save()

        messages.success(request,'Thank You!')
        return redirect('home')

    return render(request,'html/contact-us.html',{'title':'Contact Us'})


def articles_view(request):
    search = request.GET.get('search')
    tag = request.GET.get('tag')
    category = request.GET.get('category')

    if search:
        articles = Articles.objects.filter(
            Q(name__icontains=search) |
            Q(description__icontains=search) |
            Q(content__icontains=search)
        )

    elif tag:
        articles=[]
        all_articles = Articles.objects.all()
        for i in all_articles:
            if tag in [j.name for j in i.tags.all()]:
                articles.append(i)

    elif category:
        articles = Articles.objects.filter(category__name = category)[::-1]

    else:

        articles = Articles.objects.all()[::-1]
    categories = ArticleCategory.objects.all()
    tags = Tag.objects.all()


    page = request.GET.get('page')
    paginator = Paginator(articles, 9)
    try:
            articles = paginator.page(page)
    except PageNotAnInteger:
                # If page is not an integer, deliver first page.
            articles = paginator.page(1)
    except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
            articles = paginator.page(paginator.num_pages)


    return render(request,'html/blog-grid.html',{'title':'Articles','articles':articles,'categories':categories,'tags':tags})



def article_details(request,slug):
    article = Articles.objects.get(name=slug)
    categories = ArticleCategory.objects.all()
    tags = Tag.objects.all()
    articles = Articles.objects.all()[::-1][0:3]
    blog_post_url = request.build_absolute_uri(reverse('article_details', args=[slug]))

    return render(request,'html/blog-single.html',{'title':article.name,'article':article,'tags':tags,'categories':categories,'articles':articles,'blog_post_url':blog_post_url})

def aboutUs(request):
     return render(request,'html/about-us-2.html')

def career(request):
     jobs = JobPositions.objects.order_by('-id').all()
     skills = Skills.objects.all().distinct()
     search = request.GET.get('search')
     tag = request.GET.get('tag')
     if search :
            jobs = jobs.filter(
                 Q(title__icontains=search) |
            Q(sub_title__icontains=search) |
            Q(details__icontains=search) |
            Q(skills__skill__icontains=search)
            )
     elif tag:
            jobs = jobs.filter(skills__skill=tag)
            
     page = request.GET.get('page')
     paginator = Paginator(jobs, 2)
     try:
            jobs = paginator.page(page)
     except PageNotAnInteger:
                # If page is not an integer, deliver first page.
            jobs = paginator.page(1)
     except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
            jobs = paginator.page(paginator.num_pages)

     return render(request,'html/career.html',{'jobs':jobs,'title':'Career with us','skills':skills})

def career_detail(request,slug):
     job = JobPositions.objects.get(title=slug)
     if request.method == 'POST':
            id = request.POST.get('uid')
            name = request.POST.get('name')
            email = request.POST.get('email')
            contact = request.POST.get('mobile')
            experiance = request.POST.get('experiance')
            ctc = request.POST.get('ctc')
            file = request.FILES['file']
            job = JobPositions.objects.get(uid = id)
            if ApplicationsForJob.objects.filter(email=email,JobPosition=job).exists():
                 messages.error(request,"You Application is already submitted ! ")
                 return redirect('career_detail',job.title)
            
            applicant = ApplicationsForJob.objects.create(JobPosition=job,name=name,email=email,contact=contact,experiance=experiance,expected_ctc=ctc,resume=file)
            applicant.save()
            messages.success(request,"Application submitted")
            return redirect('career_detail',job.title)
     
     applicant = ApplicationsForJob.objects.filter(JobPosition=job).count()
     skills = Skills.objects.all().distinct()
     
     return render(request,'html/career-detail.html',{'job':job,'title':job.title,'applicant':applicant,'skills':skills})
    

def custom_error_view(request):
    error_message = "An error occurred. Please check your request."
    return render(request, 'html/error.html', {'error': error_message})
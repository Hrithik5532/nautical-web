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
    return render(request,"html/index.html",{'title':'Home','banner_img':banner_img})

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
        return redirect('contact_us')

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
     jobs = JobPositions.objects.all()[::-1]
     return render(request,'html/career.html',{'jobs':jobs,'title':'Career with us'})

def career_detail(request,slug):
     job = JobPositions.objects.get(title=slug)
     return render(request,'html/career-detail.html',{'job':job,'title':job.title})
from django.db import models
from ckeditor.fields import RichTextField 

from taggit.managers import TaggableManager
# Create your models here.\\

import random
import string

def generate_uid():
    # Generate a random UID with 6 characters
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))




class Banner(models.Model):
    id = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='Home-Banner/')
    headline = models.CharField(max_length=30,null=True,blank=True)
    subheadline = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.id)
    


class ContactEnquires(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=14)
    company_name = models.CharField(max_length=20, null=True,blank=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ArticleCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Articles(models.Model):
    name = models.CharField(max_length=200)
    category =models.ForeignKey(ArticleCategory,on_delete=models.CASCADE,null=True,blank=True)
    thumbnail = models.ImageField(upload_to="Article-Thumbnail/")
    writer = models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField()
    content = RichTextField(null=True, blank=True)
    created_at =models.DateField(auto_now_add=True)
    meta_tags = models.TextField()
    meta_description = models.TextField()
    tags = TaggableManager()

    def __str__(self):
        return self.name
    

class Skills(models.Model):
    skill = models.CharField(max_length=50)
    def __str__(self):
        return self.skill
    
class JobPositions(models.Model):
    uid = models.CharField(max_length=6,  default=generate_uid, editable=False)
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50,null=True,blank=True)
    salary = models.CharField(max_length=50,null=True, blank=True)
    location = models.CharField(max_length=50,null=True, blank=True)
    experiance = models.CharField(max_length=20,null=True, blank=True)
    details = RichTextField(null=True, blank=True)
    skills = models.ManyToManyField(Skills)
    last_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title
    

class ApplicationsForJob(models.Model):
    JobPosition = models.ForeignKey(JobPositions,on_delete=models.CASCADE,editable=False)
    name = models.CharField(max_length=100,editable=False)
    email =models.EmailField(editable=False)
    contact= models.CharField(max_length=15,editable=False)
    experiance = models.CharField(max_length=50,editable=False)
    expected_ctc = models.CharField(max_length=40,editable=False)
    resume = models.FileField(upload_to='Job-applicants/',editable=False)

    def __str__(self) :
        return self.name


class Services(models.Model):
    uid = models.CharField(max_length=6,  default=generate_uid, editable=False)
    img = models.FileField(upload_to='Services/')
    headline = models.CharField(max_length=100)
    description = models.TextField()
    content = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.uid
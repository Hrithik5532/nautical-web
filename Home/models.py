from django.db import models
from ckeditor.fields import RichTextField 

from taggit.managers import TaggableManager
# Create your models here.

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
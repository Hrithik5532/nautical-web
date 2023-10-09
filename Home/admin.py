from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Banner)
admin.site.register(ContactEnquires)
admin.site.register(Articles)
admin.site.register(ArticleCategory)

admin.site.register(JobPositions)

admin.site.register(Skills)
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
# Register your models here.
from .models import *

admin.site.register(Banner)
admin.site.register(ContactEnquires)
admin.site.register(Articles)
admin.site.register(ArticleCategory)

admin.site.register(JobPositions)

admin.site.register(Skills)



class ApplicationsForJobAdmin(admin.ModelAdmin):
    readonly_fields = ['job_position_details','name', 'email', 'contact', 'experiance', 'expected_ctc','resume' ]

    def job_position_details(self, obj):
        job_position = obj.JobPosition
        job_position_url = reverse("admin:Home_jobpositions_change", args=[job_position.id])
        job_position_url2 = reverse("career_detail",args=[job_position.title]) 
        return format_html('<h5>{} - {}</h5><a href="{}" target="_blank" style="margin:2px 4px; border:1px solid black; padding:3px 7px;background-color:green;color:white">Web </a><a href="{}" target="_blank" style="margin:2px 4px; border:1px solid black; padding:3px 7px;background-color:red;color:white">Database </a>', job_position.title, job_position.location,job_position_url2,job_position_url )

    job_position_details.short_description = 'Job Position Details'

    list_select_related = ('JobPosition', )

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        extra_context = extra_context or {}
        extra_context['job_position_details'] = self.job_position_details(obj)
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(ApplicationsForJob, ApplicationsForJobAdmin)

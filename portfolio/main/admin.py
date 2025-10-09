from django.contrib import admin
from .models import *

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display=['title','subtitle','description']
    
@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display=['title','description']
    
@admin.register(ExperienceSection)
class ExperienceSectionAdmin(admin.ModelAdmin):
    list_display=['title','proficiency']
    
@admin.register(ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):
    list_display=['title','description']
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','family','text','register_date','is_answered',]
    ordering=['is_answered','register_date']
    
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display=['project_name','summery_description','technologies','project_address',]

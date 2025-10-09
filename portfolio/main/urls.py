from django.urls import path
from .views import *

app_name='main'
urlpatterns = [
    path('', index,name='index'),
    path('hero-section/', render_hero_section,name='hero-section'),
    path('about-section/', render_about_section,name='about-section'),
    path('experience-section/', render_experience_section,name='experience-section'),
    path('services-section/', render_services_section,name='services-section'),
    path('contact/', ContactView.as_view(),name='contact'),
    path('projects/', get_all_projects,name='projects'),
]

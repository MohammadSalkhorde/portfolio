from django.shortcuts import render,redirect
from django.conf import settings
from .models import *
from django.views import View
from .forms import *
from django.contrib import messages

def media_admin(request):
    return {'media':settings.MEDIA_URL,}


def index(request):
    return render(request,'main/index.html')

def render_hero_section(request):
    hs=HeroSection.objects.get(id=1)
    return render(request,'partials/hero_section.html',{'hs':hs})

def render_about_section(request):
    about=AboutSection.objects.get(id=1)
    return render(request,'partials/about_section.html',{'about':about})

def render_experience_section(request):
    experience=ExperienceSection.objects.all().order_by('-proficiency')
    return render(request,'partials/experience_section.html',{'experience':experience})

def render_services_section(request):
    services=ServiceSection.objects.all()
    return render(request,'partials/services_section.html',{'services':services})


class ContactView(View):
    def get(self,request):
        form=ContactForm()
        return render(request,'partials/contact.html',{'i':form})
    
    def post(self,request):
        form=ContactForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            Contact.objects.create(
                name=cd['name'],
                family=cd['family'],
                email=cd['email'],
                phone_number=cd['phone_number'],
                text=cd['text']
            )
            #send success email
            messages.success(request,'پیام با موفقیت ارسال شد')
            return redirect('main:index')

        messages.error(request,'اطلاعات وارد شده نامعتبر میباشد','danger')
        return render(request,'partials/contact.html',{'i':form})
from django.db import models
from utils import UploadFile

#=================================================================================
class HeroSection(models.Model):
    title=models.CharField(max_length=200,verbose_name='تایتل')
    subtitle = models.CharField(max_length=255,verbose_name="عنوان تخصص")    
    description = models.TextField(verbose_name='توضیح خلاصه')   
    upload_file=UploadFile('images','hero_section')
    image_name=models.ImageField(verbose_name='تصویر',upload_to=upload_file.upload_to)   
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='بخش اصلی صفحه'                
        verbose_name_plural="بخش های اصلی صفحه"
#=================================================================================
class AboutSection(models.Model):
    title=models.CharField(max_length=250,verbose_name='تایتل')
    description = models.TextField(verbose_name='توضیحات')   
    upload_file=UploadFile('images','about_section')
    image_name=models.ImageField(verbose_name='تصویر',upload_to=upload_file.upload_to) 
    resume = models.FileField(upload_to=upload_file.upload_to, verbose_name='فایل رزومه',null=True,blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='بخش درباره من'                
        verbose_name_plural="بخش های درباره من"
#=================================================================================
class ExperienceSection(models.Model):
    title=models.CharField(max_length=50,verbose_name='تایتل')
    proficiency = models.PositiveIntegerField(verbose_name='درصد تسلط', help_text='مقدار بین 0 تا 100')

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='بخش مهارت من'                
        verbose_name_plural="بخش مهارت های من"
#=================================================================================
class ServiceSection(models.Model):
    title=models.CharField(max_length=50,verbose_name='تایتل')
    description = models.TextField(verbose_name='توضیحات')   
    upload_file=UploadFile('images','service_section')
    image_name=models.ImageField(verbose_name='تصویر',upload_to=upload_file.upload_to,null=True,blank=True) 

    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='بخش خدمات من'                
        verbose_name_plural="بخش خدمات های من"
#=================================================================================
class Contact(models.Model):
    name=models.CharField(max_length=50,verbose_name='نام')
    family=models.CharField(max_length=50,verbose_name='نام خانوادگی')
    email=models.EmailField(verbose_name='ایمیل')
    phone_number=models.CharField(max_length=11,verbose_name='شماره تلفن')
    text=models.TextField(verbose_name='متن')
    register_date=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ثبت')
    is_answered = models.BooleanField(default=False, verbose_name='پاسخ داده شده')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='پیام'                
        verbose_name_plural="پیام ها"
#=================================================================================
class Projects(models.Model):
    project_name=models.CharField(max_length=100,verbose_name='نام پروژه')
    upload_file=UploadFile('images','projects')
    image_name=models.ImageField(verbose_name='تصویر',upload_to=upload_file.upload_to,null=True,blank=True) 
    summery_description=models.TextField(verbose_name='خلاصه توضیحات')
    description=models.TextField(verbose_name='توضیحات')
    technologies=models.TextField(verbose_name='فناوری ها')
    project_address=models.URLField(verbose_name='آدرس پروژه')

    def __str__(self):
        return self.project_name
    
    class Meta:
        verbose_name='پروژه'                
        verbose_name_plural="پروژه ها"
#=================================================================================

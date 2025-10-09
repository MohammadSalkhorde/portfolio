from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label="",
                         widget=forms.TextInput())
    family=forms.CharField(label="",
                         widget=forms.TextInput())
    email=forms.CharField(label="",
                         widget=forms.EmailInput())
    phone_number=forms.CharField(label="",
                         widget=forms.TextInput())
    text=forms.CharField(label="",
                         widget=forms.Textarea())
    

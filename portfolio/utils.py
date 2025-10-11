#----------------------------------------------------------------------
#----------------------------------------------------------------------
# from kavenegar import *

# def send_sms(mobile,message):
    # api = KavenegarAPI('')
    # params = { 'sender' : '2000660110', 'receptor': mobile, 'message' :message }
    # response = api.sms_send(params)
    # pass
#----------------------------------------------------------------------
#----------------------------------------------------------------------
from uuid import uuid4
import os

class UploadFile:
    def __init__(self,dir,prefix):
        self.dir = dir
        self.prefix = prefix
    
    def upload_to(self,instance,filename):
        filename, ext =os.path.splitext(filename)
        return f'{self.dir}/{self.prefix}/{uuid4()}{ext}'
#----------------------------------------------------------------------
from django.core.mail import send_mail

from django.core.mail import EmailMessage

from django.core.mail import EmailMessage

def send_email(user_email, user_name, user_message):
    subject = "Thanks for Contacting Me!"

    html_message = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f7f7f7;
                color: #333;
                line-height: 1.6;
            }}
            .container {{
                max-width: 600px;
                margin: 20px auto;
                background-color: #ffffff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }}
            .logo {{
                text-align: center;
                margin-bottom: 20px;
            }}
            h1 {{
                color: #2c3e50;
            }}
            p {{
                margin-bottom: 15px;
            }}
            .footer {{
                margin-top: 20px;
                font-size: 12px;
                color: #888;
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">
                <img src="https://mohammad-salkhorde.ir/media/images/logo/light-mode.png" 
                    alt="Logo" style="height: 60px;">
            </div>
            <h1>Hi {user_name},</h1>
            <p>Thanks for getting in touch! I’ve received your message:</p>
            <blockquote style="background: #f1f1f1; padding: 10px; border-left: 4px solid #2c3e50;">
                {user_message}
            </blockquote>
            <p>I really appreciate your interest and will get back to you as soon as possible.</p>
            <p>Cheers,<br><strong>Mohammad Salkhorde</strong></p>
            <div class="footer">
                This is an automated confirmation from Mohammad Salkhorde's personal portfolio website.
            </div>
        </div>
    </body>
    </html>
    """

    email = EmailMessage(
        subject=subject,
        body=html_message,
        from_email='info@mohammad-salkhorde.ir',
        to=[user_email],
    )
    email.content_subtype = "html"  # مهم برای HTML
    email.send()


#----------------------------------------------------------------------

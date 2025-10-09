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
#----------------------------------------------------------------------
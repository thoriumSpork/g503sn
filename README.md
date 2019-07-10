# g503sn
An application for the registration and display of user-submitted World War 2 military jeep data organized by serial number  
  
This branch is for the Django version of the backend.  
  
so don't merge.  
  
Please exclude \migrations from commits  
a file \g503sndb\local_settings.py is required to be added. please exclude it from commits.  
contents are  
  
import os  
SECRET_KEY = '<your secret >'  
  
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': '< your database name >',  
        'USER': '< your db user>',  
        'PASSWORD': '< your wavy washers >',  
        'HOST': '< your db server >',   # Or an IP Address that your DB is hosted on  
        'PORT': '3306',  
    }  
}  

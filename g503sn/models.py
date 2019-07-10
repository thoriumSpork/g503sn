# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime
from django.utils import timezone
from .choices import *

class SerialNumbers(models.Model):
    xid = models.AutoField(primary_key=True)
    xmodel = models.IntegerField(verbose_name='Model',choices=MODEL_CHOICES,blank=False,default='Bantam BRC')
    xserialnumber = models.IntegerField(verbose_name='Serial Number')
    xframe = models.CharField(verbose_name='Frame #', max_length=25, blank=True, null=True)
    xengine = models.CharField(verbose_name='Engine #',max_length=25, blank=True, null=True)
    xbody = models.CharField(verbose_name='Body #',max_length=25, blank=False, choices=BODY_TYPE_CHOICES,default='Unknown')
    xbodytype = models.CharField(verbose_name='Body Type',max_length=50, blank=True, null=True)
    xhood = models.CharField(verbose_name='Hood #',max_length=25, blank=True, null=True)
    xfactory = models.CharField(verbose_name='Factory',max_length=50, blank=True, null=True)
    xweight = models.CharField(verbose_name='Weight',max_length=50, blank=True, null=True)
    xplateorigin = models.CharField(verbose_name='Plate Origin',max_length=50, blank=False, choices=DATA_PLATE_ORIGIN_CHOICES, default='First')
    xplate = models.CharField(verbose_name='Plate',max_length=50, blank=False, choices=DATA_PLATE_MATERIAL_CHOICES,default='Unknown')
    xdateofmanufacture = models.DateField(verbose_name='Date of Manufacture')
    xdateofacquisition = models.DateField(verbose_name='Date you aquired this machine')
    xfirstname = models.CharField(verbose_name='First Name',max_length=50, blank=True, null=True)
    xlastname = models.CharField(verbose_name='Last Name',max_length=50, blank=True, null=True)
    xemail = models.CharField(verbose_name='eMail Address',max_length=50, blank=True, null=True)
    xprivatemessage = models.IntegerField(verbose_name='Allow Private Message',blank=False,choices=PRIVATE_MESSAGE_CHOICES,default='Yes')
    xphone = models.CharField(verbose_name='Phone',max_length=50, blank=True, null=True)
    xcity = models.CharField(verbose_name='City',max_length=50, blank=True, null=True)
    xstate = models.CharField(verbose_name='State',max_length=50, blank=True, null=True)
    xcountry = models.IntegerField()
    xpassword = models.CharField(verbose_name='Password',max_length=50, blank=True, null=True)
    ximagesmall = models.CharField(verbose_name='Image small',max_length=50, blank=True, null=True)
    ximagemedium = models.CharField(verbose_name='Image medium',max_length=50, blank=True, null=True)
    ximagelarge = models.CharField(verbose_name='Image Large',max_length=50, blank=True, null=True)
    xblurb = models.TextField(verbose_name='Blurb',blank=True, null=True)
    xdetails = models.TextField(verbose_name='Details',blank=True, null=True)
    xurl = models.CharField(verbose_name='URL',max_length=128, blank=True, null=True)
    xtopicid = models.IntegerField()
    xip = models.CharField(verbose_name='IP Address',max_length=50, blank=True, null=True)
    xspotlightcount = models.IntegerField()
    xactive = models.IntegerField()
    xdatecreated = models.DateTimeField()
    xdatemodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'serialnumbers_tbl'
        verbose_name = 'Serial Number'
        verbose_name_plural = 'Serial Numbers'
        ordering = ['xmodel','xserialnumber']

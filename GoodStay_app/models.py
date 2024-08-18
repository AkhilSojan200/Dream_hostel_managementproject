
from django.contrib.auth.models import AbstractUser, Login
# from django.utils.html import escape, make_safe

from django.db import models

# Create your models here.

class Login(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_warden = models.BooleanField(default=False)



class Custom_student(models.Model):

    name = models.CharField(max_length=250,blank=True,null=True)
    address = models.CharField(max_length=250,blank=True,null=True)
    phone_no = models.IntegerField(null=True,blank=True)


class Custom_warden(models.Model):

    name=models.CharField(max_length=250,blank=True,null=True)
    address = models.CharField(max_length=250,blank=True,null=True)
    phone_no = models.IntegerField(null=True,blank=True)
    occupation = models.CharField(max_length=250,blank=True,null=True)


class RoomDetails(models.Model):

    Room_no = models.CharField(max_length=250, blank=True, null=True)
    details = models.CharField(max_length=250,blank=True,null=True)
    Block_name = models.CharField(max_length=250, blank=True, null=True)
    No_of_beds = models.CharField(max_length=250, blank=True, null=True)
    Monthly_fee = models.CharField(max_length=250, blank=True, null=True)
    image = models.FileField(upload_to='uploads/')


class Complaints(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=250, blank=True, null=True)
    complaint = models.TextField(max_length=250, blank=True, null=True)
    date = models.DateField( blank=True, null=True)
    reply = models.TextField(max_length=250, blank=True, null=True)


class Schedule(models.Model):
    user = models.ForeignKey(Custom_warden, on_delete=models.DO_NOTHING)
    hostel = models.ForeignKey(RoomDetails, on_delete=models.DO_NOTHING)
    date_in = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)


class Notification(models.Model):
    date = models.DateField(blank=True, null=True)
    notice_heading = models.CharField(max_length=250,blank=True,null=True)
    notice_details = models.TextField(max_length=250,blank=True,null=True)



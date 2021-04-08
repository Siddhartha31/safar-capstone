import os
import uuid
from django.utils.timezone import now
from datetime import datetime
from django.contrib.auth.models import User

from django.db import models

class Account(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=200)

    def __str__(self):
        return str(self.fullname)


class Admin(models.Model):
    admin_username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=False)
    admin_fullname = models.CharField(max_length=200)
    admin_phone = models.CharField(max_length=12)
    admin_email = models.CharField(max_length=200)

    def __str__(self):
        return str(self.admin_username)



def get_file_address(instance, filename):
    return '/'.join(['supporting',str(instance.account_id),str(instance.uuid), filename])

class Request(models.Model):
    CATEGORY = (
        ('MEDICAL', 'MEDICAL'),
        ('PHYSICAL HELP', 'PHYSICAL HELP'),
        ('OTHER', 'OTHER')
    )
    STATUS = (
        ('PENDING', 'PENDING'),
        ('ACCEPTED', 'ACCEPTED'),
        ('CANCELLED', 'CANCELLED'),
        ('COMPLETED', 'COMPLETED')
    )
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    request_category = models.CharField(max_length=50, default="OTHER", choices=CATEGORY)
    amount = models.FloatField(default=0)
    collected = models.FloatField(default=0)
    desc = models.CharField(max_length=200, default='No Description')
    identity_image = models.ImageField(upload_to=get_file_address, null=True, blank=True)
    image1 = models.ImageField(upload_to=get_file_address, null=True, blank=True)
    image2 = models.ImageField(upload_to=get_file_address, null=True, blank=True)
    deadline = models.DateField()
    status = models.CharField(max_length=50, default="PENDING", choices=STATUS)
    pub_date = models.DateTimeField(default=now)
    admin_msg = models.CharField(max_length=200, default='none',null=True)
    
    def __str__(self):
        return str(self.id)


class Accept(models.Model):
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE, null=True)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True)


class Payment(models.Model):
    STATUS = (
        ('PENDING', 'PENDING'),
        ('SUCCESSFUL', 'SUCCESSFUL'),
        ('FAILED', 'FAILED'),
    )
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE, null=True)
    amount = models.FloatField(default=0)
    status = models.CharField(max_length=50, default="PENDING", choices=STATUS)
    date = models.DateTimeField(default=now)



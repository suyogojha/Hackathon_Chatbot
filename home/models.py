from django.db import models
from django.db.models.deletion import CASCADE

from twilio.rest import Client

# Create your models here.
from datetime import datetime

# Create your models here.


class doctorname(models.Model):
    name = models.CharField(max_length=255, null=True,blank=True)
    contact = models.CharField(max_length=255, null=True,blank=True)
    address = models.CharField(max_length=255, null=True,blank=True)
    email = models.EmailField(max_length=255, null=True,blank=True)
    
    def __str__(self):
        return self.name


class appointment(models.Model):
    departments = models.CharField(max_length=255, null=True,blank=True)
    name = models.CharField(max_length=255, null=True,blank=True)
    email = models.EmailField(max_length=255, null=True,blank=True)
    contact = models.CharField(max_length=255, null=True,blank=True)
    address = models.CharField(max_length=255, null=True,blank=True)
    sex = models.CharField(max_length=255, null=True,blank=True)
    Age = models.CharField(max_length=255, null=True,blank=True)
    doctorname = models.ForeignKey(doctorname, on_delete=CASCADE, null=True,blank=True)
    yourdetails = models.CharField(max_length=255, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name









class message(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    contact = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.contact >= 10:
            account_sid = 'ACc704a2d7d5aa87747aeb499632ee789d'
            auth_token = '77c9d73b4434adfa26f721a37b34bf02'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Congratulations {self.name},your appontment has been registered for doctor dipesh\n UserName:dipesh\n  Password:dipeshthapa123 ",
                from_='+18788796403',
                to='+977-9814327222'
            )
        else:
            account_sid = 'ACc704a2d7d5aa87747aeb499632ee789d'
            auth_token = '77c9d73b4434adfa26f721a37b34bf02'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Congratulations {self.name},your appontment has been registered for doctor suyog\n UserName:suyog\n  Password:suyogojha123 ",
                from_='+18788796403',
                to='+977-9814327222'
            )
            
        print(message.sid)
        return super().save(*args, **kwargs)
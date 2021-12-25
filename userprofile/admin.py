from django.contrib import admin
from django.contrib.admin.decorators import register
from userprofile.models import profile

# Register your models here.
@admin.register(profile)
class userprofileAdmin(admin.ModelAdmin):
    list_display = ("user", "name")
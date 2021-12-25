from django.contrib import admin
from home.models import appointment, doctorname



# Register your models here.
@admin.register(appointment)
class appointmentAdmin(admin.ModelAdmin):
    list_display = ("departments", "doctorname", "name", "email", "contact", "address", "sex", "Age", "yourdetails", "created_at")
    list_filter = ("name",)
    search_fields = ["name"]


@admin.register(doctorname)
class doctornameAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "email", "address")
    list_filter = ("name",)
    search_fields = ["name"]






from home.models import message

# Register your models here.
@admin.register(message)
class messageAdmin(admin.ModelAdmin):
    list_display = ("name", "contact")
    list_filter = ("contact",)
    search_fields = ["name"]
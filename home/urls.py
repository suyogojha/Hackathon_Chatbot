from django.contrib import admin
from django.urls import path
from home.views import home, appointment, about, contact, service, add_product, get_tocken, chat
from . import views

app_name  = "home"

admin.site.site_header  = "Doctor Talk"
admin.site.site_header  = "Doctor Talk Dashboard"
admin.site.index_title  = "welcome to the Doctor Talk Dashboard"

urlpatterns = [
    path('', home, name="home"),
    path('appointment/', appointment, name="appointment"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('service/', service, name="service"),
    path('chat/', chat, name="chat"),
    path('add_product/', add_product, name="add_product"),
    path('get_tocken/', get_tocken, name="get_tocken"),

]




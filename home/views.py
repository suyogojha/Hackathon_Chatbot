from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from home.models import appointment
from home.models import appointment, message
from home.forms import doctorForm, TokenForm

# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def chat(request):
    return render(request, "chat.html")
    


def contact(request):
    return render(request, "contact.html")


def service(request):
    return render(request, "service.html")


def add_product(request):
    form = doctorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        appointment.objects.create(**form.cleaned_data)
        return HttpResponseRedirect(reverse("home:home"))
    return render(request, "form.html", {"form": form})


def get_tocken(request):
    form = TokenForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        print(form.cleaned_data)
        message.objects.create(**form.cleaned_data)
        return HttpResponseRedirect(reverse("home:home"))
    return render(request, "form.html", {"form": form})








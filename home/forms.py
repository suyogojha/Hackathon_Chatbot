from django import forms
from home.models import appointment, message
from django.db import models


class doctorForm(forms.ModelForm):
    class Meta:
        model = appointment
        fields = "__all__"
        

class TokenForm(forms.ModelForm):
    class Meta:
        model = message
        fields = "__all__"
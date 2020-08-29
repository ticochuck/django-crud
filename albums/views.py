from django import forms
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from .models import Records

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class CreatePageView(CreateView):
    template_name = 'create.html'
    model = Records
    #fields = ['title', 'artist', 'description']
    fields = "__all__"

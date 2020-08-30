from django import forms
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import Records

# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = Records


class CreatePageView(CreateView):
    template_name = 'create.html'
    model = Records
    fields = "__all__"


class DetailPageView(DetailView):
    template_name = 'detail_view.html'
    model = Records


class UpdatePageView(UpdateView):
    template_name = 'update.html'
    fields = "__all__"
    model = Records


class DeletePageView(DeleteView):
    template_name = 'delete.html'
    model = Records
    success_url = reverse_lazy('home')

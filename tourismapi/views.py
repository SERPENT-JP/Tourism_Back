from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Prefecture

class IndexView(ListView):
    template_name = "index.html"
    model = Prefecture 

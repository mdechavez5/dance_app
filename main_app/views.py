from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class DancerList(TemplateView):
    template_name = "dancer_list.html"


from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from searching_app.models import Restaurants




class HomePageView(TemplateView):
    template_name = 'home.html'

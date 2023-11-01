from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from websiteapp.models import GalleryImage

# Create your views here.

class HomeView(TemplateView):
    template_name = 'websiteapp/home.html'


class AboutView(TemplateView):
    template_name = 'websiteapp/about.html'




class SkillsView(TemplateView):
    template_name = 'websiteapp/skills.html'


class WorkView(TemplateView):
    template_name = 'websiteapp/work.html'



class ContactView(TemplateView):
    template_name = 'websiteapp/contact.html'

class GalleryListView(ListView):
    model = GalleryImage
    template_name = 'websiteapp/gallery.html'
    context_object_name = 'images'
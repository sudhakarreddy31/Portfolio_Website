from django.urls import path
from . import views
from .views import AboutView, ContactView, GalleryListView, HomeView, SkillsView, WorkView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='About'),
    path('skills', SkillsView.as_view(), name='Skills'),
    path('work', WorkView.as_view(), name='Work'),
    path('contact', ContactView.as_view(), name='Contact'),
    path('gallery', GalleryListView.as_view(), name='Gallery'),
]
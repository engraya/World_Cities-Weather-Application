# here we are import path from in-built django-urls
from django.urls import path

# here we are importing all the Views from the views.py file
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.homePage, name='homePage'),
    path('basePage/', views.basePage, name='basePage'),
    path('contactPage/', views.contactPage, name='contactPage'),
    path('updatePage/', views.updatePage, name='updatePage'),
    path('componentsPage/', views.componentsPage, name='componentsPage'),
    path('updatePage/', views.updatePage, name='updatePage'),
    path('newsPage/', views.newsPage, name='newsPage'),
    path('apiPage/', views.apiPage, name='apiPage'),
    path('galleryPage/', views.galleryPage, name='galleryPage'),
    path('errorPage/', views.errorPage, name='errorPage'),
]

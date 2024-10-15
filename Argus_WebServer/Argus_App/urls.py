from os import path
from django.urls import path, include
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('', lambda request: redirect('/mash/'), name='home'),
    path('<slug:slug>/', views.fill_template_from_db, name='main'),
]
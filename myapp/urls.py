#app-url.py
from django.contrib import admin
from django.urls import path

# ============  REST FRAMEWORK ========
from myapp import views
from django.urls import include, path
from rest_framework import routers

# ============================================
urlpatterns = [
    path('', views.main, name = 'main'),
    path('listing/', views.listing, name = 'listing'),
    path('searching/', views.searching, name = 'searching'),
    path('searching/show_result', views.show_result),
    ]

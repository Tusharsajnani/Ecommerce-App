from django.contrib import admin
from django.urls import path,include
from store.views import *
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('cart/', views.Cartview.as_view()),
    path('cart/<int:pk>/', views.Cartcrud.as_view()),
]
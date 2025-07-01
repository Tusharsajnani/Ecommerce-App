from django.contrib import admin
from django.urls import path,include
from store.views import *
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('',views.Shipmentview.as_view())
]
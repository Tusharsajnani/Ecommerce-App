from django.contrib import admin
from django.urls import path
from store.views import *
from store.orders.views import Orderview
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
      path('', Orderview.as_view())
]
from django.contrib import admin
from django.urls import path,include
from store.views import *
# from . import views
from store.payment.views import Paymentview

urlpatterns=[
      path('',Paymentview.as_view())
]
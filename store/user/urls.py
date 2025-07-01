# urlpatterns = [
#     path('users',views.get_all_user,name='get_all_users'),                 #GET
#     path('create',views.create_user,name='create_user'),                   #POST
#     path('<int:pk>',views.get_all_users_by_ID,name='get_all_users_by_ID'), #GET by ID
#     path('<int:pk>/update', views.update_user, name='update_user'),        #PUT
#     path('<int:pk>/delete', views.delete_user, name='delete_user')         #DELETE

# ]

from django.contrib import admin
from django.urls import path,include
from store.views import *
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.Userview.as_view()),
    path('get_user/<int:pk>', views.Usercrud.as_view())

]

# urlpatterns = format_suffix_patterns(urlpatterns)
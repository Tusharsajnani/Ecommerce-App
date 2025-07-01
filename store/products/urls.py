from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.add_product),            # Handles POST request
    path('all/', views.get_all_products),   # Handles GET request
]

# urlpatterns = format_suffix_patterns(urlpatterns)

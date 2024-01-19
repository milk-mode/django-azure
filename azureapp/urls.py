from django.urls import path
from .views import display_data

urlpatterns = [
    path('display/', display_data, name='display_data'),
]
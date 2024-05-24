# lights/urls.py

from django.urls import path
from .views import lamp_list, lamp_detail

urlpatterns = [
    path('', lamp_list, name='lamp_list'),
    path('lamp/<int:lamp_id>/', lamp_detail, name='lamp_detail'),
]

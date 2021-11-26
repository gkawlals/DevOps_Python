from django.urls import path, re_path
from . import views

urlpatterns=[
    re_path(r'(20[0-1][0-9]|202[0-1])$', views.year),
    re_path(r'(0[1-9]|1[0-2])$', views.month),
]
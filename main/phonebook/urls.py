from django.urls import path, re_path
from . import views

app_name = "PB" # phonebook의 약어 PB

urlpatterns = [
    path('index/', views.index, name='IndexUrl'),
    path('add/', views.add, name='AddUrl'),
    re_path(r'^delete/(\d+)/$', views.delete, name='DeleteUrl'),
    re_path(r'^detail/(\d+)/$', views.detail, name='DetailUrl'),
    re_path(r'^update/(\d+)/$', views.update, name='UpdateUrl'),
    re_path(r'^PBdetail/(\d+)/$', views.PBdetail, name='PBDetailUrl'),
]
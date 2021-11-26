from django.urls import path, re_path
from . import views

app_name = 'BD'

urlpatterns=[
    path("",views.index, name="BIndex"),
    re_path(r'^(\d+)/$',views.detail, name="BDetail"),
    re_path(r'^(\d+)/update/$',views.update, name="BUpdate"),
    re_path(r'^(\d+)/delete/$',views.delete, name="BDelete"),
    path('add/',views.add, name="BAdd"),
]
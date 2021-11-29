from django.urls import path, re_path
from . import views

app_name = 'BD'

urlpatterns=[
    re_path(r"^page/(\d+)/$",views.index, name="BIndex"),
    re_path(r'^(\d+)/$',views.detail, name="BDetail"),
    re_path(r'^(\d+)/update/$',views.update, name="BUpdate"),
    re_path(r'^(\d+)/delete/$',views.delete, name="BDelete"),
    path('add/',views.add, name="BAdd"),
    path('updown/upload',views.upload),
    path('updown/',views.updown),
    path('updown/download/<filename>',views.download, name='down'),
]
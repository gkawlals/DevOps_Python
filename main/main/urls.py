
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('phonebook/', include('phonebook.urls')),
    path("",views.index, name='start' ),
    path('account/', include('django.contrib.auth.urls')),
    path('account/register', views.createAccount, name='createAccount'),
    path('account/myinfo', views.myinfo, name='myinfo'),
    path('account/deleteuser', views.deleteuser, name='deleteuser'),
    path('test',views.test),
    path('board/', include('board.urls')),
]

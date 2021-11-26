"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path("", views.index),
    path("notice/", views.notice),
    #path("board/<int:boardId>", views.board),
    path("language/<lang>", views.language),
    re_path(r'reg1/(.)/', views.reg1),
    re_path(r'reg2/(..)/', views.reg2),
    re_path(r'reg3/(.{5})/', views.reg3),
    re_path(r'reg4/(.{3}|.{5})/', views.reg4),
    re_path(r'reg5/(.{3,5})/', views.reg5),
    re_path(r'reg6(.+)/', views.reg6),
    re_path(r'reg7(.*)/', views.reg7),
    re_path(r'reg8/([0-9])/', views.reg8),
    re_path(r'reg9/([0-9][0-9][0-9])/', views.reg9),
    re_path(r'reg10/([0-9]{3})/', views.reg10),
    re_path(r'reg11/(20[0-1][0-9]|20[2][0-1])/', views.reg11),
    re_path(r'reg12/([a-zA-Z0-9ㄱ-힣]+)/', views.reg12),
    re_path(r'reg13/(010|011|012)-([0-9]{4}-[0-9]{4})/', views.reg13),
    re_path(r'reg14/(\d+)',views.reg14),
    re_path(r'reg15/(\w+)',views.reg15),
    re_path(r'email/(\w+[@]\w+[.]\w{3}|\w+[@]\w+[.]\w+[.]\w+)', views.email),
    re_path(r'lang/(ko|en|jp)/', views.lang),
    path('board/', include('board.urls')),
    path('chart/', include('chart.urls')),
    path('temp1/', views.temp1),
    path('temp2/', views.temp2),
    path('temp3/', views.temp3),
    path('quiz1/', views.quiz1),
    path('quiz2/', views.quiz2),
    path('quiz3/', views.quiz3),
    path('image/', views.image),
]

# language 경로를 입력 하면
# language/en, language/ko, language/jp
# en : 영어, ko : 한국어, jp : 일본어
# 그외에는 알수없는 언어 출력

# email 경로를 입력하고 email 형식으로 입력받기
# language 경로를 입력하면 ko, en, jp 만 입력받기
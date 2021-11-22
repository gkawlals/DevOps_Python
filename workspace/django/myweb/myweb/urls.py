
from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path("",views.index),
    path("notice/",views.notice),
    path("board/<int:boardId>", views.board),
    path("language/<lang>", views.language),
    # 정규화의 대한 예시 
    re_path(r'reg1/(.)/',views.reg1),# 한 글자 입력 받기 
    re_path(r'reg2/(..)/',views.reg2), # 2글자 입력받ㅂ기
    re_path(r'reg3/(.{5})/',views.reg3), # 5글자 입력받기 
    re_path(r'reg4/(.{3}|.{5})/',views.reg4), # 3 또는 5글자의 문자 입력받기
    re_path(r'reg5/(.{3,5})/',views.reg5), # 3~5문자 입력받기 
    re_path(r'reg6(.+)/',views.reg6), # 하나 이상의 문자 입력받기
    re_path(r'reg7(.*)/',views.reg7), # 0개 이상의 문자 입력받기 
    re_path(r'reg8/([0-9])/',views.reg8),
    re_path(r'reg9/([0-9]{3})/',views.reg9), # or [0-9][0-9][0-9] 000~999만 받아오기
    re_path(r'reg10/([2][0][0-1][0-9]|[2][0][1-2][0-1])/',views.reg10),
    re_path(r'reg11/([a-zA-Z0-9ㄱ-힣]+)/',views.reg11),
    re_path(r'reg12/(010-[0-9]{4}-[0-9]{4})/',views.reg12),
    # 계획서의 맞게 각각의 페이지 그려보기 
]

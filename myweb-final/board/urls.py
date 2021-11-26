from django.urls import path, re_path
from . import views

urlpatterns=[
    path('test', views.test),
    re_path(r'(\d+)', views.boarder),
]

# board/숫자가 들어오면 '숫자 페이지 입니다.' 출력
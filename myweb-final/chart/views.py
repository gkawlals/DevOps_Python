from django import http
from django.shortcuts import render, HttpResponse

# Create your views here.
def year(request, year):
    message = year + " 년도 페이지 입니다.";
    return HttpResponse(message);

def month(request, mon):
    message = mon + " 월 페이지 입니다.";
    return HttpResponse(message);
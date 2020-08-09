from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import pymysql,re


def hello(request):
    return HttpResponse("Hello world ! ")


def default(request):
    return HttpResponse("Hello world  by default! ")
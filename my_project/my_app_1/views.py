from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a sample from <strong>my_app_1</strong>")


def otherpage(request):
    return HttpResponse("Now you are at <strong>otherpage</strong>")

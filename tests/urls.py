from django.http import HttpResponse
from django.urls import path

# from http import HTTPStatus


def index(request):
    return HttpResponse("hello world")


def ping(request):
    return HttpResponse("pong")


urlpatterns = [
    path("", index),
    path("ping", ping),
]

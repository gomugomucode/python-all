from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("This is the  home page bhaaiya ")

def about(request):
    return HttpResponse("This is the  about page bhaaiya ")

def service(request):
    return HttpResponse("This is the  service page bhaaiya ")

def contact(request):
    return HttpResponse("This is the  contact page bhaaiya ")
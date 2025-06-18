from django.shortcuts import render, HttpResponse

def index(request):
    return render(request , 'index.html')
    # return HttpResponse("This is the  home page bhaaiya ")

def about(request):
    return render(request , 'about.html')

def service(request):
    return render(request , 'service.html')
def contact(request):
    return render(request , 'contact.html')
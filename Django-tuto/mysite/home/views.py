from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from datetime import datetime


def index(request):
    # messages.success(request, "test msg")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')
from django.shortcuts import render, redirect
from .models import Contact  # Make sure this model exists in models.py
from django.contrib import messages
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        sub = request.POST.get('sub')
        msg = request.POST.get('msg')

        # Save the data to the database
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            sub=sub,      
            msg=msg ,
            date=datetime.today()
        )
        contact.save()
        messages.success(request,"Your message has been sent !")

        return redirect('contact')  # Redirect to avoid resubmission on refresh

    return render(request, 'contact.html')

from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['sub']
            message = form.cleaned_data['msg']

            full_subject = f"{subject} from {name}"
            try:
                send_mail(
                    full_subject,
                    message,
                    email,
                    ['baralanupam111@gmail.com'], 
                    fail_silently=False
                )
                messages.success(request, " Your message has been sent!")
            except BadHeaderError:
                messages.error(request, " Invalid header found. Message not sent.")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

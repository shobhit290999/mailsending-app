
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

def home(request):
    return render(request,"home.html")

def subscribe(request):
   
    if request.method == 'POST':
            subject = 'Code Band'
            message = 'i love you'
            recipient = request.POST.get('email', '')
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            
            return redirect('reademail/subscribe')
    return render(request, 'subscriptions/home.html')


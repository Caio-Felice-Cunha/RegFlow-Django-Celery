from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
from django.core.mail import send_mail

def subscription(request):
    return render(request, 'subscription.html')

def aplicationprocess(request):
    name = request.POST.get('name')
    email = request.POST.get('email')

    person = Person(name=name, email=email)
    person.save()

    send_mail(
        'IASUMMIT | Subscription Received',
        'Your application has been received. Thank you for your interest in IASUMMIT!',
        'caiofcunha@hotmail.com',
        recipient_list=[email]
    )

    return HttpResponse(f"Name: {name}, Email: {email}")


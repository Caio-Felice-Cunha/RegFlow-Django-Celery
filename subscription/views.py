from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
from django.core.mail import send_mail
from django.conf import settings
import os
from PIL import Image, ImageDraw, ImageFont
from hashlib import sha256
from .tasks import create_invitation
from django.db import IntegrityError


def subscription(request):
    return render(request, 'subscription.html')

def aplicationprocess(request):
    name = request.POST.get('name')
    email = request.POST.get('email')

    # Check if email already exists
    if Person.objects.filter(email=email).exists():
        return render(request, 'subscription.html', {
            'error': 'This email is already registered for the event.',
            'name': name,  # Return the name to preserve the form data
            'email': email  # Return the email to preserve the form data
        })

    # If email doesn't exist, proceed with registration
    person = Person(name=name, email=email)
    person.save()
    token = create_invitation.delay(name, email)
    
    return render(request, 'register_confirmed.html', {'token': token})

def index(request):
    return render(request, 'index.html')


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
            'name': name,
            'email': email
        })

    # If email doesn't exist, proceed with registration
    person = Person(name=name, email=email)
    person.save()
    
    # Execute the task and get the token
    task_result = create_invitation.delay(name, email)
    token = task_result.get()  # Wait for the task to complete and get the token
    
    return render(request, 'register_confirmed.html', {'token': token})

def index(request):
    return render(request, 'index.html')


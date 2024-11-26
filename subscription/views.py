from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
from django.core.mail import send_mail
from django.conf import settings
import os
from PIL import Image, ImageDraw, ImageFont
from hashlib import sha256
from .tasks import create_invitation


def subscription(request):
    return render(request, 'subscription.html')

def aplicationprocess(request):

    name = request.POST.get('name')
    email = request.POST.get('email')

    token = create_invitation.delay(name, email)

    person = Person(name=name, email=email)
    person.save()

    return render(request, 'register_confirmed.html', {'token': token})


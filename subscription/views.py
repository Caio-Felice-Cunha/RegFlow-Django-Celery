from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
from django.core.mail import send_mail
from django.conf import settings
import os
from PIL import Image, ImageDraw, ImageFont
from hashlib import sha256

def subscription(request):
    return render(request, 'subscription.html')

def aplicationprocess(request):

    def create_invitation(name, email):
        template = os.path.join(settings.STATIC_ROOT, 'img/invitation.png')
        img = Image.open(template)
        draw = ImageDraw.Draw(img)
        
        # Get image dimensions
        width, height = img.size
        
        # Load Terminal font from Windows system fonts
        font_path = os.path.join(os.environ['SYSTEMROOT'], 'Fonts', 'consola.ttf')  # Consolas
        font = ImageFont.truetype(font_path, 60)  
        
        # Get text size to center it
        text_bbox = draw.textbbox((0, 0), name, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Calculate center position
        x = (width - text_width) / 2
        y = 100
        
        # Draw text centered
        draw.text((x, y), name.upper(), fill='white', font=font)

        secret_key = "SAS21516*!&@CSAC!*@&C4@CS@(85)"
        token = sha256(email.encode() + secret_key.encode()).hexdigest()

        img.save(os.path.join(settings.MEDIA_ROOT, f'invitations/{token}.png'))

        return token


    name = request.POST.get('name')
    email = request.POST.get('email')

    token = create_invitation(name, email)

    person = Person(name=name, email=email)
    person.save()

    send_mail(
        'IASUMMIT | Subscription Received',
        'Your application has been received. Thank you for your interest in IASUMMIT!',
        'events@iasummit.com.br',
        recipient_list=[email]
    )

    return render(request, 'register_confirmed.html', {'token': token})


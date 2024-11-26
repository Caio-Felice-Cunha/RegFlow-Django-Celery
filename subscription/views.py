from django.http import HttpResponse
from django.shortcuts import render
from .models import Person

def subscription(request):
    return render(request, 'subscription.html')

def aplicationprocess(request):
    name = request.POST.get('name')
    email = request.POST.get('email')

    person = Person(name=name, email=email)
    person.save()

    return HttpResponse(f"Name: {name}, Email: {email}")


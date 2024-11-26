from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.subscription, name='subscription'),
    path('aplicationprocess/', views.aplicationprocess, name='aplicationprocess'),
]
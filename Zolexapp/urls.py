from django.urls import path #importing the necessary documents

from . import views

app_name ='Zolexapp'

urlpatterns = [
path('', views.index, name='index'),
]
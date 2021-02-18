from django.urls import path, include
from .views import *

urlpatterns = [
    path('', information, name='information'),
    path('Book_Details/', bookDetails, name='bookDetails'),
    path('howToTakenBook/', howToTakenBook, name='howToTakenBook'),


]

from django.urls import path
from .views import *
urlpatterns = [
    path('', busDetails, name='busDetails'),
    path('payment/', payment, name='payment'),
    path('blog/', blog, name='blog'),
    path('home/', home, name='home'),
    path('profile/', profile, name='profile'),



]

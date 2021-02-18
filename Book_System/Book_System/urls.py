
from django.contrib import admin
from django.urls import path, include
import accounts.views


# from django.Book_System.accounts.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts.views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('store/', include('store.urls'))

]


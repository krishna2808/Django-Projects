from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
import bus.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bus.views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('bus/', include('bus.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

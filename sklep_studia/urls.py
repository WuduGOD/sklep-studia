from django.contrib import admin
from django.urls import path
from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # <- TO MUSI BYĆ!
    path('', views.home, name='home'),
]

# Obsługa plików multimedialnych w trybie developerskim
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

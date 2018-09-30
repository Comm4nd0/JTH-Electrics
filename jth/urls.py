from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about-us', views.about, name='about'),
    path('contact/', include('contact.urls')),
    path('services', views.services, name='services'),
    path('services_detials', views.services_details, name='services_details'),
    path('copyright', views.copyright, name='copyright'),
    path('privacy-policy', views.privacypolicy, name='privacypolicy'),
    path('terms-and-conditions', views.terms, name='terms'),
    path('cookies', views.cookies, name='cookies'),
    path('projects/', include('projects.urls')),
    path('', views.contact_form, name='contact_form')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

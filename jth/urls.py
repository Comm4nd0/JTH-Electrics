from django.contrib import admin
from django.urls import path, include
from pages import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about-us', views.about, name='about'),
    path('contact/', include('contact.urls')),
    path('', views.contact_form, name='contact_form')
]

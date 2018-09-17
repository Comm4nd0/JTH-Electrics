from django.shortcuts import render
from .models import ContactDetail


def contact(request):
    contact_details = ContactDetail.objects.first()
    return render(request, 'contact.html', {'contact_detail': contact_details})
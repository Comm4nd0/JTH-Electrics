from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
import json
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def services_details(request):
    return render(request, 'services_details.html')

def copyright(request):
    return render(request, 'copyright.html')

def privacypolicy(request):
    return render(request, 'privacy_policy.html')

def terms(request):
    return render(request, 'terms&conditions.html')

def cookies(request):
    return render(request, 'cookies.html')

def contact_form(request):
    if request.POST:
        print('this')
        email = EmailMessage(
            request.POST.get('subject'),
            "{}, {}".format(request.POST.get('message'), request.POST.get('message')),
            'contact@cmdlb.com',
            ['marcobaldanza@hotmail.co.uk'],
            # ['johnnyb@jthelectrics.co.uk'],
            reply_to=[request.POST['email']],
        )

        try:
            email.send(fail_silently=False)
            message = {'message': "Thank you for your email, we'll be in touch soon!"}
        except:
            message = {'message': "Something went wrong, but we're working on it!"}

        return HttpResponse(json.dumps(message), content_type='application/json')
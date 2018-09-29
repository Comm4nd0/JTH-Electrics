from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
import json
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

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
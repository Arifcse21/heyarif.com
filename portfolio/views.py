from django.shortcuts import render, redirect
from django.conf import settings
from .forms import PingForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            print(name,email,subject,message)
            
            send_mail(subject, message, settings.EMAIL_HOST_USER, ['arifcse21@gmail.com',])
    else:
        form = PingForm()

    return render(request, 'portfolio/index.html', {'form': form})

# def thanks(request):
#     return render(request, 'portfolio/thanks.html',{data:"Thanks for message"})
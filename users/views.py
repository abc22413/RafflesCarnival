from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
import sys

def validate_captcha(captcha_response):
    return True

# Create your views here.
def LoginView(request):
    context = {}
    if request.method == "GET":
        return render(request, 'login.html')
    
    elif request.method == "POST":
        form = request.POST
        captcha_response = form.get("g-recaptcha-response")
        if not validate_captcha(captcha_response):
            context["captcha_fail"]=True
        username = form.get("username")
        password = form.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_page = form.get("next")
            return HttpResponseRedirect(next_page if next_page else reverse('home'))
        else:
            context["login_fail"]=True
        return render(request, 'login.html', context=context)
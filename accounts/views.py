from django.shortcuts import render, HttpResponse
from accounts.models import Register
from datetime import datetime
from django.contrib.auth.models import User,  auth

# Create your views here.
def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        user = Register(name=name, email=email, mobile=mobile, password=password, date = datetime.today())
        if password == repassword:
             user.save()
    return render(request, 'register.html')
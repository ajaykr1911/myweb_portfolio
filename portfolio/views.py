from django.shortcuts import render, HttpResponse
from datetime import date, datetime
from portfolio.models import Contact

# Create your views here.

def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date = datetime.today())
        contact.save()

    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html')

def cv(request): 
    return render(request, 'cv.html')
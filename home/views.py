from curses.ascii import HT
from multiprocessing import context
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        "variable" : "This is varaible"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is Homepage")


def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is about Page")

def blog(request):
    return render(request,'blog.html')
    # return HttpResponse("This is blog page")

def contact(request):
    if request.method == "POST":
        username =  request.POST.get('username')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        desc = request.POST.get('desc')
        contact = Contact(username = username,email=email,address=address,city=city,state=state,zip=zip,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'contact.html')
    # return HttpResponse("This is Contact page")
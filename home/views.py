from curses.ascii import HT
from multiprocessing import context
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable" : "This is varaible"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is Homepage")


def sendex(request):
    return HttpResponse("This is sendex")

def about(request):
    return HttpResponse("This is about")
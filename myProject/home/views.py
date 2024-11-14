
from django.http import HttpResponse
from django.shortcuts import render
from home.models import Settings


# Create your views here.
def index(request):
    context = {"page":"home"}
    return render(request,'index.html',context)

def iletisim(request):
    
    context = {"page":"Contact"}
    return render(request, 'iletisim.html', context)

def aboutus(request):
    context = {"sayfa": "About Us "}
    return render(request, 'aboutus.html', context)
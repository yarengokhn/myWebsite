
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.forms import ContactForm
from home.models import ContactFormMessage, Settings
from product.models import Product


# Create your views here.
def index(request):
    slider = Product.objects.filter(status=True).order_by('?')[:4]
    trendy_product = Product.objects.order_by('viewcount')[:20]
    context = {"page": "home",'trendy_product':trendy_product,
               "slider": slider}
    
    return render(request,'index.html',context)

def iletisim(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.subject = form.cleaned_data['subject']
            data.ip = request.META['REMOTE_ADDR']#is a key in this dictionary that holds the IP address of the client (i.e., the user's device) that initiated the request.
            data.save()
            messages.success(request, 'Mesajınız Başarıyla İletilmiştir')
            return HttpResponseRedirect('/iletisim')
        else:
            messages.error(request, 'Mesajınız Sisteme Kaydedilmemiştir')
            return HttpResponseRedirect('/iletisim')
    form = ContactForm()
    context = {"page":"Contact",
               "form": form}
    return render(request, 'iletisim.html', context)

def aboutus(request):
    context = {"page": "About Us "}
    return render(request, 'aboutus.html', context)


def checkout(request):
    context = {"page": "Check out "}
    return render(request, 'checking_out.html', context)
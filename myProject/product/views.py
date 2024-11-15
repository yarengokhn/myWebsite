from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from product.forms import SearchForm
from product.models import Category, Images, Product


# Create your views here.
def index(request):
    return HttpResponse(" ")

def categoryProducts(request,id,slug):
    category=Category.objects.get(pk=id)

    products_in_category = Product.objects.filter(product_category = id)
    context = {
        'productsInCategory': products_in_category,  # Bu kategorideki ürünler listesi
        'category': category   # Kategorinin kendisi
    }
    return render(request, 'kategori_urunler.html', context)



def productDetail(request,id,slug):
    
    product = Product.objects.get(id=id)
    product.viewcount = product.viewcount + 1
    product.save()


    images = Images.objects.filter(id =id)
    category=Category.objects.get(pk=id)

    products_in_category = Product.objects.filter(product_category =product.product_category)

    context = {
        'product': product,
        'images':images,
        'category': category ,  # Kategorinin kendisi
        'productsInCategory': products_in_category,  # Bu kategorideki ürünler listesi
    }
    return render(request, 'product_detail.html', context)



def search(request):
    if request.method =='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query =form.cleaned_data['query']
            results =Product.objects.filter(title__icontains = query)
            context = {'results':results}
            return render(request, 'search.html', context)
    return HttpResponseRedirect('/')

        


from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from product.forms import CommentForm, SearchForm
from product.models import Category, Comment, Images, Product


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

    comments =Comment.objects.filter(product_id = id)# o ürüne ait yorumlar 

    form=CommentForm

    context = {
        'product': product,
        'images':images,
        'comments':comments,
        'category': category ,  # Kategorinin kendisi
        'productsInCategory': products_in_category, # Bu kategorideki ürünler listesi
        'form':form 
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

def addcomment(request,id):
    #HTTP_REFERER, kullanıcının şu anki sayfaya hangi URL'den geldiğini belirtir. 
    url =request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.comment = form.cleaned_data['comment']
            comment.product_id = id
            comment.user = request.user
            comment.subject = form.cleaned_data['subject']
            comment.rate = int(form.cleaned_data['rate'])
            comment.ip = request.META.get('REMOTE_ADDR')
            comment.save()
            messages.success(request, 'yorum ekleme başarılı')
            return HttpResponseRedirect(url)
    else:
        messages.error(request, 'yorum ekleme Başarısız')
        return HttpResponseRedirect(url)




        


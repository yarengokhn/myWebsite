"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from home import views as homeviews
from product import views as productviews

from myProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('',homeviews.index,name = 'index'),#name='index': URL’e kolayca referans vermek için bir isim tanımlar.
    path('iletisim', homeviews.iletisim, name='iletisim'),
    path('aboutus', homeviews.aboutus, name='aboutus'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('product/<int:id>/<slug:slug>/', productviews.productDetail, name='productDetail'),
    path('category/<int:id>/<slug:slug>/', productviews.categoryProducts, name='categoryProducts' ),
    
]  +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
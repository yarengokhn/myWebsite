from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class Category(models.Model):
    STATUS = (('True', 'Evet'),('False', 'Hayir')) #Kategori aktif/pasif durumu 
    #Kategori aktif durumda. Bu durumda kategori siteye eklenir ve kullanıcılar tarafından görülebilir,Kategori pasif durumda. Bu durumda kategori sitede görünmez.
    title = models.CharField(max_length=25)
    keywords = models.CharField(blank=True, max_length=300)
    description = models.CharField(blank=True, max_length=300)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children', on_delete=models.CASCADE)
   
    create_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    discount_tag = models.CharField(max_length=30, blank =True, null = True)
    filter_options = models.JSONField(blank=True, null=True) 


    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS=( ('True','Evet'),('False','Hayir'))

    product_category =models.ForeignKey(Category,on_delete=models.CASCADE) #her ürün bir kategoriye ait olacak.
    #Product modelini Category modeline bağlar ve bir kategori silindiğinde o kategoriye ait tüm ürünlerin de silinmesini sağlar.
    user =models.ForeignKey(User,on_delete = models.CASCADE)
    title=models.CharField(max_length=75)
    keywords=models.CharField(blank=True,max_length=300)
    description=models.CharField(blank=True,max_length=300)
    image=models.ImageField(blank=True,upload_to='images/')
    price=models.FloatField()
    amount=models.IntegerField(default=0)
    detail=models.TextField()
    status=models.CharField(max_length=10,choices=STATUS,default='False')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    slug=models.SlugField(null=False,unique=True)

    def thumbnail(self):
        if self.image:
            return mark_safe('<img src="{}" width="50"/>'.format(self.image.url))
        return "No Image"
# mark_safe() HTML çıktısını güvenli hale getiren bir fonksiyondur.
    
    thumbnail.short_description = 'Image' #bu sütunun başlığı olarak "Image" metni gösterilir.

    def __str__(self):
        return self.title

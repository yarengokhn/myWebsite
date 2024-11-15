from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

# Create your models here.

class Category(MPTTModel):
    STATUS = (('True', 'Evet'),('False', 'Hayir')) #Kategori aktif/pasif durumu 
    #Kategori aktif durumda. Bu durumda kategori siteye eklenir ve kullanıcılar tarafından görülebilir,Kategori pasif durumda. Bu durumda kategori sitede görünmez.
    title = models.CharField(max_length=25)
    keywords = models.CharField(blank=True, max_length=300)
    description = models.CharField(blank=True, max_length=300)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)

    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
   
    create_at=models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    discount_tag = models.CharField(max_length=30, blank =True, null = True)
    filter_options = models.JSONField(blank=True, null=True) 

    class MPTTMeta:
     order_insertion_by = ['title'] 


    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '/'.join(full_path)
       


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

    detail=RichTextUploadingField()
    status=models.CharField(max_length=10,choices=STATUS,default='False')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    slug=models.SlugField(null=False,unique=True)
    
    viewcount=models.IntegerField(default=0)

    def thumbnail(self):
        if self.image:
            return mark_safe('<img src="{}" width="50"/>'.format(self.image.url))
        return "No Image"
# mark_safe() HTML çıktısını güvenli hale getiren bir fonksiyondur.
    
    thumbnail.short_description = 'Image' #bu sütunun başlığı olarak "Image" metni gösterilir.


    def image_preview(self):
        if self.image:
            return format_html('<img src="{}" style="width: 300px; height: auto;" />', self.image.url)
        return '-'
    image_preview.short_description = 'Current Image'



    def __str__(self):
        return self.title
    

class Images(models.Model):

    product=models.ForeignKey(Product,on_delete=models.CASCADE) #her resim bir Ürün ile ilişkilidir, ancak her ürün birden fazla resim  ile ilişkilendirilebilir.
    title = models.CharField(max_length=30)
    image=models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
    
    
    def image_tag(self):
        return mark_safe('<img src="{}" width="50"/>'.format(self.image.url))
    

    image_tag.short_description = 'Image'

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250, blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject
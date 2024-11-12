from django.db import models

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
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

    discount_tag = models.CharField(max_length=30, blank =True, null = True)
    filter_options = models.JSONField(blank=True, null=True) 


    def __str__(self):
        return self.title


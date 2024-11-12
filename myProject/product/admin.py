from django.contrib import admin
from product.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    prepopulated_fields = {"slug": ("title","keywords")}
    search_fields = ['title','keywords'] # admin paneline bir arama kutusu ekler ve title veya keywords alanlarına göre arama yapılmasını sağlar
    list_editable = ['status'] # liste görünümünden doğrudan düzenlenebilme
    readonly_fields = ['create_at','update_at']




admin.site.register(Category,CategoryAdmin)



class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','price','amount']
    list_filter = ['status','product_category']
    prepopulated_fields = {"slug": ("product_category","title")}
    search_fields = ['product_category','title','keywords'] # admin paneline bir arama kutusu ekler ve title veya keywords alanlarına göre arama yapılmasını sağlar
    list_editable = ['status'] # liste görünümünden doğrudan düzenlenebilme
    readonly_fields = ['price']




admin.site.register(Product,ProductAdmin)
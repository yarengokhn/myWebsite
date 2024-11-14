from django.contrib import admin
from product.models import Category, Images, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    prepopulated_fields = {"slug": ("title","keywords")}
    search_fields = ['title','keywords'] # admin paneline bir arama kutusu ekler ve title veya keywords alanlarına göre arama yapılmasını sağlar
    list_editable = ['status'] # liste görünümünden doğrudan düzenlenebilme
    readonly_fields = ['create_at','update_at']




class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)
        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs
    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'
    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'
    pass

admin.site.register(Category, CategoryAdmin2)



class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 10
    readonly_fields = ('image_tag',)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status','price','amount','thumbnail']
    list_filter = ['status','product_category']
    inlines =[ProductImagesInline]
    prepopulated_fields = {"slug": ("product_category","title")}
    search_fields = ['product_category','title','keywords'] # admin paneline bir arama kutusu ekler ve title veya keywords alanlarına göre arama yapılmasını sağlar
    list_editable = ['status'] # liste görünümünden doğrudan düzenlenebilme
    readonly_fields = ['thumbnail']

    


admin.site.register(Product,ProductAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'image_tag']
    readonly_fields = ['image_tag']


admin.site.register(Images, ImageAdmin)


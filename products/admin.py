from django.contrib import admin
from products.models import ProductCategory, Product, Basket
admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #what wil be shown not inside of panel
    list_display = ('name', 'price', 'quantity', 'category')
    #how fields will be structured inside
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')
    #fields where you can type a name and find what you want
    search_fields = ('name',)
    #how your fields will be ordered like order_by method
    ordering = ('-name',)



class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', )
    extra = 0

from django.contrib import admin

from .models import Genre, Artist, Product

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
        list_display = ['name', 'slug']
        prepopulated_fields = {'slug': ('name',)}

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
        list_display = ['name', 'slug']
        prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
        list_display = ['title', 'artist', 'slug', 'price', 'available', 'created', 'updated']
        list_filter = ['available', 'is_active']  
        list_editable = ['price', 'available']            
        prepopulated_fields = {'slug': ('title',)}
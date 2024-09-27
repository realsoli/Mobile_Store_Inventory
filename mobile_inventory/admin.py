from django.contrib import admin
from .models import Phone, Color, Brand, Country


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['model', 'brand', 'color', 'country_of_manufacture', 'price', 'is_available']
    search_fields = ['model', 'brand__name', 'color__name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'nationality']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']

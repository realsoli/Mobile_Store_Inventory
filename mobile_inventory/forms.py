from .models import Phone, Brand, Color, Country
from django import forms


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'nationality']

    error_messages = {
        'name': {
            'required': 'برند الزامی لدلب.',
            'unique': 'این برند از قبل موجود است.'
        }}


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']

    error_messages = {
        'country': {
            'required': 'کشور الزامی است.',
        }}


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name']
        error_messages = {
            'name': {
                'required': 'رنگ الزامی است.',
                'unique': 'این رنگ  وجود دارد.'
            }
        }


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'

        error_messages = {
            'model': {
                'required': 'مدل الزامی است.',
            },
            'brand': {
                'required': 'برند الزامی است.',
            },
            'color': {
                'required': 'رنگ الزامی است.',
            },
            'country_of_manufacture': {
                'required': 'کشور سازنده الزامی است.',
            },
            'price': {
                'required': 'قیمت الزامی است.',

            },
            'image': {
                'required': 'تصویر الزامی است.',
            },
            'screen_size': {
                'required': 'سایز صفحه نمایش الزامی است.',
            },
        }

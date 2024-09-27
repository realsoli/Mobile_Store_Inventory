from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نام برند')
    nationality = models.CharField(max_length=100, verbose_name='ملیت برند')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = ' برند ها'


class Color(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='رنگ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نام کشور')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'کشور'
        verbose_name_plural = 'کشورها'


class Phone(models.Model):
    model = models.CharField(max_length=100, unique=True, verbose_name='مدل')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='برند')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='رنگ')
    country_of_manufacture = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='کشور سازنده')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to='phone_images', null=True, blank=True, verbose_name='تصویر')
    screen_size = models.FloatField(verbose_name='سایز صفحه نمایش')
    is_available = models.BooleanField(default=True, verbose_name='موجود/ناموجود')

    def __str__(self):
        availability = 'موجود' if self.is_available else 'ناموجود'
        return f"{self.brand.name} {self.model} - {availability}"

    class Meta:
        verbose_name = 'موبایل'
        verbose_name_plural = 'موبایل ها'

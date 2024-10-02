import itertools

from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نام برند')
    nationality = models.CharField(max_length=100, verbose_name='ملیت برند')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, verbose_name='آدرس برند')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            # استفاده از unidecode برای تبدیل حروف فارسی به لاتین
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = ' برند ها'


class Color(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='رنگ')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, verbose_name='آدرس رنگ')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            # استفاده از unidecode برای تبدیل حروف فارسی به لاتین
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نام کشور')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, verbose_name='آدرس کشور')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            # استفاده از unidecode برای تبدیل حروف فارسی به لاتین
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

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
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, verbose_name='آدرس محصول')

    def __str__(self):
        availability = 'موجود' if self.is_available else 'ناموجود'
        return f"{self.brand.name} {self.model} - {availability}"

    # تولید slug به صورت خودکار
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(unidecode(f"{self.model}-{self.color}"))
            slug = base_slug
            # چک کردن برای جلوگیری از تکراری بودن slug
            for i in itertools.count(1):
                if not Phone.objects.filter(slug=slug).exists():
                    break
                slug = f"{base_slug}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'موبایل'
        verbose_name_plural = 'موبایل ها'

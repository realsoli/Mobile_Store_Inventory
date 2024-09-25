from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.nationality}'


class Color(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Phone(models.Model):
    model = models.CharField(max_length=100, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='phone_images', null=True, blank=True)
    screen_size = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        availability = 'Available' if self.is_available else 'Sold'
        return f"{self.brand.name} {self.model} - {availability}"

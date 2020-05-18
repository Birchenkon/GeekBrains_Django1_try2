from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __set__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='product_img', blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='кол-во на складе', default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class Contact(models.Model):
    phone = models.CharField(max_length=32, verbose_name='номер телефона')
    email = models.EmailField(max_length=128, verbose_name='email')
    city = models.CharField(max_length=32, default='Москва', verbose_name='город')
    address = models.CharField(max_length=128, verbose_name='адрес')

    def __str__(self):
        return f"{self.pk} {self.email}"

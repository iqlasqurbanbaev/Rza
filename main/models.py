from django.db import models


class Main(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    text = models.TextField()
    image = models.ImageField(upload_to='main/%Y/%m/%d')

    def __str__(self) -> str:
        return self.first_name

class Product(models.Model):
    name = models.CharField(max_length=45)
    anons = models.CharField(max_length=150)
    status = models.BooleanField()
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=4)
    slug = models.SlugField(max_length=125, null=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=45, verbose_name='Category name')
    slug = models.SlugField(max_length=125)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return f'/menu/category/{self.slug}'


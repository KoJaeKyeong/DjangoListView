from django.db import models


# Create your models here.
class Closet(models.Model):
    brand = models.CharField('Brand', max_length=100, blank=True)
    classification = models.CharField('classification', max_length=100, blank=True)
    product_name = models.CharField('Product Name', max_length=100, blank=True)
    product_image = models.URLField('Image URL', unique=True)

    def __str__(self):
        return self.product_name

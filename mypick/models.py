from django.db import models


# Create your models here.
class Mypick(models.Model):
    top_brand = models.CharField('Top Brand', max_length=100, blank=True)
    top_product_name = models.CharField('Top Product Name', max_length=100, blank=True)
    top_image = models.URLField('Top Image URL', unique=True,default='')
    pants_brand = models.CharField('Pants Brand', max_length=100, blank=True)
    pants_product_name = models.CharField('Pants Product Name', max_length=100, blank=True)
    pants_image = models.URLField('Pants Image URL', unique=True)

    def __str__(self):
        return self.top_product_name

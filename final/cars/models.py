from PIL import Image
import uuid
from django.db import models
from django.contrib.auth.models import User




class Entity(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(editable=False, auto_now=True)


class Brands(Entity):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Car(Entity):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    mudel = models.IntegerField()
    transmission = models.CharField(max_length=100)
    engin_size = models.CharField(max_length=100)
    powerBHP = models.CharField(max_length=100)
    distance_meter = models.CharField(max_length=100)
    discription = models.TextField()
    price = models.FloatField()
    is_salled = models.BooleanField('is salled')
    user = models.ForeignKey(User, verbose_name='user', related_name='cars', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands, verbose_name='brands', related_name='cars', on_delete=models.CASCADE)
    # seats
    # licence_plate


    def __str__(self):
        return self.name



class Images(Entity):
    image = models.ImageField('image', upload_to='car/')
    car = models.ForeignKey(Car, verbose_name='car', related_name='images',on_delete=models.CASCADE)


    def __str__(self):
        return self.car.name


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Order_item(Entity):
    user = models.ForeignKey(User, verbose_name='user', related_name='order_items', on_delete=models.CASCADE)
    car = models.ForeignKey('cars.Car', verbose_name='car',
                                on_delete=models.CASCADE)
    total = models.DecimalField('total', blank=True, null=True, max_digits=1000, decimal_places=0)
    note = models.CharField('note', null=True, blank=True, max_length=100)
    ordered = models.BooleanField('ordered')


    def __str__(self):
        return self.car.name


class Favorite(Entity):
    user = models.ForeignKey(User, verbose_name='user', related_name='favorites', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, verbose_name='car', related_name='favorites',on_delete=models.CASCADE)


    def __str__(self):
        return self.car.name
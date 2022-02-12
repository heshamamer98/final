from operator import imod
from django.contrib import admin


from cars.models import Brands, Car, Images, Order_item



admin.site.register(Brands)
admin.site.register(Car)
admin.site.register(Images)
admin.site.register(Order_item)
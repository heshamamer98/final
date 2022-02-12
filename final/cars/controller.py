from typing import List
from unicodedata import name
from django.shortcuts import render
from ninja import Router
from cars.schema import BrandsOut, MessageOut, CarOut, ImageOut, OrderItemOut, AddBrands
from cars.models import Brands, Car, Images, Order_item

cars_controller = Router()

'''
GET /resources?name=hesham&age=23       #query pqrqmeter
GET /resources/{id}                     path parameter
POST /resources 
PUT /resources/{id}
DELET /resources/{id}

#body
{} - json object
'''

@cars_controller.get('list_brands', response={
        200:List[BrandsOut],
        404: MessageOut
    })
def list_brands(request):

    brands = Brands.objects.all()
    if brands:
        return brands
    else:
        return 404, {'detail': 'No brands yet'}



@cars_controller.get('list_cars', response={
        200:List[CarOut],
        404: MessageOut
    })
def list_cars(request):
    
    cars = Car.objects.all()
    if cars:
        return cars
    else:
        return 404, {'detail': 'No cars yet'}



@cars_controller.get('list_images', response={
        200:List[ImageOut],
        404: MessageOut
    })
def list_images(request):
    
    images = Images.objects.all()
    if images:
        return images
    else:
        return 404, {'detail': 'No images yet'}


@cars_controller.get('list_OrderItem', response={
        200:List[OrderItemOut],
        404: MessageOut
    })
def list_images(request):

    Ordered_items = Order_item.objects.all()
    if Ordered_items:
        return Ordered_items
    else:
        return 404, {'detail': 'No Ordered items yet'}



@cars_controller.post('addBrand', response={
        201: BrandsOut,
        400: MessageOut
    })
def create_brand(request, brand_in: AddBrands):
    brand = Brands(**brand_in.dict())
    is_saved = brand.save()
    if is_saved:
        return 400, {'detail': 'Brand not saved'}
    else:
        return 201, brand
    


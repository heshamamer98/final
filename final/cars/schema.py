from pydantic import UUID4
from ninja import ModelSchema, Schema
from django.contrib.auth.models import User


class MessageOut(Schema):
    detail : str


class UUIDSchema(Schema):
    id: UUID4


class UserOut(ModelSchema):
    class Config:
        model = User
        model_fields = ['id', 'username']
        # model_exclude = ['created', 'updated']            # else this fields


class BrandsOut(UUIDSchema):
    name : str


class AddBrands(Schema):
    name : str


class CarOut(UUIDSchema):
    name : str
    color: str
    status: str
    mudel: int
    transmission: str
    engin_size: str
    powerBHP: str
    distance_meter: str
    discription: str
    price: float
    is_salled: bool
    user: UserOut
    brand: BrandsOut


class ImageCarOut(UUIDSchema):
    name : str


class ImageOut(UUIDSchema):
    image: str
    car: ImageCarOut


class OrderItemOut(UUIDSchema):
    user: UserOut
    car: ImageCarOut
    total: float
    note: str
    ordered: bool

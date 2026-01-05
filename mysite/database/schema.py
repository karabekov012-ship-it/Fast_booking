from pydantic import BaseModel, EmailStr
from typing import Optional
from .models import RoleChoice, RoomTypeChoice, RoomStatusChoices
from datetime import date, datetime


class CountryInputSchema(BaseModel):
    country_image: str
    country_name: str

class CountryOutSchema(BaseModel):
    id: int
    country_image: str
    country_name: str


class UserProfileInputSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    country_id: int
    email: EmailStr
    password: str
    age: Optional[int]
    phone_number: Optional[str]

class UserProfileOutSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    age: Optional[int]
    phone_number: Optional[str]
    role: RoleChoice
    date_registered: date

class UserLoginSchema(BaseModel):
    username: str
    password: str


class CityInputSchema(BaseModel):
    city_name: str
    city_image: str
    city_id: int

class CityOutSchema(BaseModel):
    id: int
    city_name: str
    city_image: str
    city_id: int


class ServiceInputSchema(BaseModel):
    service_name: str
    service_image: str

class ServiceOutSchema(BaseModel):
    id: int
    service_name: str
    service_image: str


class HotelInputSchema(BaseModel):
    city_id: int
    hotel_name: str
    street: str
    postal_code: str
    hotel_stars: str
    description: str

class HotelOutSchema(BaseModel):
    id: int
    hotel_name: str
    street: str
    postal_code: str
    hotel_stars: str
    description: str


class HotelImageInputSchema(BaseModel):
    image: str
    hotel_id: int

class HotelImageOutSchema(BaseModel):
    id: int
    image: str
    hotel_id: int


class RoomInputSchema(BaseModel):
    hotel_id: int
    room_number: str
    price: int
    type: RoomTypeChoice
    room_status: RoomStatusChoices
    description: str

class RoomOutSchema(BaseModel):
    id: int
    room_number: str
    price: int
    type: RoomTypeChoice
    room_status: RoomStatusChoices
    description: str

class RoomImageInputSchema(BaseModel):
    image: str
    room_id: int

class RoomImageOutSchema(BaseModel):
    id: int
    image: str
    room_id: int


class ReviewInputSchema(BaseModel):
    user_id: int
    hotel_id: int
    comment: str
    rating: int

class ReviewOutSchema(BaseModel):
    id: int
    user_id: int
    hotel_id: int
    comment: str
    rating: int
    created_date: datetime


class BookingInputSchema(BaseModel):
    user_id: int
    hotel_id: int
    room_id: int
    check_in: date
    check_out: date
    create_date: date

class BookingOutSchema(BaseModel):
    id: int
    user_id: int
    hotel_id: int
    room_id: int
    check_in: date
    check_out: date
    create_date: date

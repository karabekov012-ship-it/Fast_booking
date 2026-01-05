from mysite.database.models import (UserProfile, RefreshToken, City, Service,
                                    Country, Hotel ,HotelImage, Room , RoomImage, Review, Booking)
from sqladmin import ModelView

class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.id, UserProfile.first_name, UserProfile.last_name, UserProfile.username, UserProfile.age, UserProfile.phone_number, UserProfile.role, UserProfile.date_registered, UserProfile.email, UserProfile.password, UserProfile.country_id]

class RefreshTokenAdmin(ModelView, model=RefreshToken):
    column_list = [RefreshToken.id, RefreshToken.created_date]

class CityAdmin(ModelView, model=City):
    column_list = [City.id, City.city_name, City.city_image]

class ServiceAdmin(ModelView, model=Service):
    column_list = [Service.id, Service.service_name, Service.service_image]

class CountryAdmin(ModelView, model=Country):
    column_list = [Country.id, Country.country_name, Country.country_image]

class HotelAdmin(ModelView, model=Hotel):
    column_list = [Hotel.id, Hotel.hotel_name, Hotel.street, Hotel.description,]

class HotelImageAdmin(ModelView, model=HotelImage):
    column_list = [HotelImage.id, HotelImage.image]

class RoomAdmin(ModelView, model=Room):
    column_list = [Room.id, Room.price, Room.room_number, Room.type, Room.room_status, Room.description ]

class RoomImageAdmin(ModelView, model=RoomImage):
    column_list = [RoomImage.id, RoomImage.image]

class ReviewAdmin(ModelView, model=Review):
    column_list = [Review.id, Review.rating, Review.comment, Review.create_date]

class BookingAdmin(ModelView, model=Booking):
    column_list = [Booking.id, Booking.create_date]
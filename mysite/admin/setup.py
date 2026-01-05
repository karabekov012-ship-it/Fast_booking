from .views import (UserProfileAdmin,RefreshTokenAdmin, CityAdmin,
                    ServiceAdmin, CountryAdmin, HotelAdmin, HotelImageAdmin,
                    RoomAdmin, RoomImageAdmin,ReviewAdmin, BookingAdmin)
from fastapi import FastAPI
from sqladmin import Admin
from mysite.database.db import engine

def setup_admin(my_site: FastAPI):
    admin = Admin(my_site, engine)
    admin.add_view(UserProfileAdmin)
    admin.add_view(RefreshTokenAdmin)
    admin.add_view(CityAdmin)
    admin.add_view(ServiceAdmin)
    admin.add_view(CountryAdmin)
    admin.add_view(HotelAdmin)
    admin.add_view(HotelImageAdmin)
    admin.add_view(RoomAdmin)
    admin.add_view(RoomImageAdmin)
    admin.add_view(ReviewAdmin)
    admin.add_view(BookingAdmin)
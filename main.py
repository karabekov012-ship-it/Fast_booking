from fastapi import FastAPI
from mysite.api import auth, user, country, city, service, hotel, hotel_image, room, room_image, review, booking
from mysite.admin.setup import setup_admin
import uvicorn

hotels_app = FastAPI(title="Hotel book")
setup_admin(hotels_app)
hotels_app.include_router(auth.auth_router)
hotels_app.include_router(user.user_router)
hotels_app.include_router(country.country_router)
hotels_app.include_router(city.city_router)
hotels_app.include_router(service.service_router)
hotels_app.include_router(hotel.hotel_router)
hotels_app.include_router(hotel_image.hotel_image_router)
hotels_app.include_router(room.room_router)
hotels_app.include_router(room_image.room_image_router)
hotels_app.include_router(review.review_router)
hotels_app.include_router(booking.booking_router)

if __name__ == '__main__':
    uvicorn.run(hotels_app, host="127.0.0.1", port=8000)


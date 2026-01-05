from sqlalchemy.testing.pickleable import User
from .db import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Date, Enum, ForeignKey, Text, DateTime
from typing import Optional, List
from enum import Enum as PyEnum
from datetime import date, datetime

class RoleChoice(str, PyEnum):
    client = 'client'
    owner = 'owner'


class Country(Base):
    __tablename__ = 'countries'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    country_image: Mapped [str] = mapped_column(String)
    country_name: Mapped[str] = mapped_column(String(30), unique=True)

    user_country: Mapped[List['UserProfile']] = relationship('UserProfile',
                                                             back_populates='country',
                                                             cascade="all, delete-orphan")
    cities: Mapped[List['City']] = relationship('City',
                                                back_populates='country_city',
                                                cascade="all, delete-orphan")



class UserProfile(Base):
    __tablename__ = 'profile'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    country_id: Mapped[int] = mapped_column(ForeignKey('countries.id'))
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    age: Mapped[Optional [int]] = mapped_column(Integer, nullable=True)
    phone_number: Mapped[Optional [str]] = mapped_column(String, nullable=True)
    role: Mapped[RoleChoice] = mapped_column(Enum(RoleChoice), default=RoleChoice.client)
    date_registered: Mapped[date] = mapped_column(Date, default=date.today)

    country: Mapped[Country] = relationship(back_populates="user_country",)
    user_review: Mapped[List['Review']] = relationship(back_populates='user',
                                                       cascade='all, delete-orphan')
    user_token: Mapped[List['RefreshToken']] = relationship(back_populates='token_user',
                                                            cascade='all, delete-orphan')


class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    token_user: Mapped[UserProfile] = relationship(UserProfile,back_populates='user_token')
    token: Mapped[str] = mapped_column(String)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow())


class City(Base):
    __tablename__ = 'cities'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    city_name: Mapped[str] = mapped_column(String(30), unique=True)
    city_image: Mapped [str] = mapped_column(String)
    country_id: Mapped[int] = mapped_column(ForeignKey('countries.id'))

    country_city: Mapped[Country] = relationship(Country, back_populates='cities')
    hotels: Mapped[List['Hotel']] = relationship(back_populates='city',
                                                 cascade="all, delete-orphan")

class Service(Base):
    __tablename__ = 'services'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    service_name: Mapped[str] = mapped_column(String(30), unique=True)
    service_image: Mapped [str] = mapped_column(String)

class Hotel(Base):
    __tablename__ = 'hotels'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    city_id: Mapped[int] = mapped_column(ForeignKey('cities.id'))
    hotel_name: Mapped[str] = mapped_column(String)
    street: Mapped[str] = mapped_column(String(100))
    postal_code: Mapped[int] = mapped_column(Integer)
    hotel_stars: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(Text)

    city: Mapped[City] = relationship(City, back_populates='hotels')
    images: Mapped[List['HotelImage']] = relationship(back_populates='hotel',
                                                       cascade="all, delete-orphan")
    rooms: Mapped[List['Room']] = relationship(back_populates='hotel_rooms',
                                             cascade="all, delete-orphan")
    hotel_review: Mapped[List['Review']] = relationship(back_populates='hotel_reviews',
                                                        cascade="all, delete-orphan")
    hotel_booking: Mapped[List['Booking']] = relationship(back_populates='hotel_bookings',
                                                        cascade="all, delete-orphan")

class HotelImage(Base):
    __tablename__ = 'hotel_images'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    image: Mapped [str] = mapped_column(String)
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))

    hotel: Mapped[Hotel] = relationship(Hotel, back_populates='images')

class RoomTypeChoice(str, PyEnum):
    Suite = 'Suite'
    Junior_Suite = 'Junior_Suite'
    Family_Room = 'Family_Room'
    Economy = 'Economy'
    Single_Room = 'Single_Room'

class RoomStatusChoices(str, PyEnum):
    Occupied = 'Occupied'
    Reserved = 'Reserved'
    Available = 'Available'

class Room(Base):
    __tablename__ = 'room'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))
    room_number: Mapped[int] = mapped_column(Integer)
    price: Mapped[int] = mapped_column(Integer)
    type: Mapped[RoomTypeChoice] = mapped_column(Enum(RoomTypeChoice))
    room_status: Mapped[RoomStatusChoices] = mapped_column(Enum(RoomStatusChoices))
    description: Mapped[str] = mapped_column(Text)

    hotel_rooms: Mapped[Hotel] = relationship(Hotel, back_populates='rooms')
    images: Mapped[List[RoomImage]] = relationship(back_populates='room',
                                                   cascade="all, delete-orphan")
    room_booking: Mapped[List[Booking]] = relationship(back_populates='room_bookings',
                                                        cascade="all, delete-orphan")


class RoomImage(Base):
    __tablename__ = 'room_images'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    image: Mapped[str] = mapped_column(String)
    room_id: Mapped[int] = mapped_column(ForeignKey('room.id'))

    room: Mapped[Room] = relationship(Room, back_populates='images')

class Review(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))
    rating: Mapped[int] = mapped_column(Integer)
    comment: Mapped[str] = mapped_column(String)
    create_date: Mapped[date] = mapped_column(Date, default=date.today)

    user: Mapped[User] = relationship(UserProfile, back_populates='user_review')
    hotel_reviews: Mapped[Hotel] = relationship(Hotel, back_populates='hotel_review')

class Booking(Base):
    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('profile.id'))
    hotel_id: Mapped[int] = mapped_column(ForeignKey('hotels.id'))
    room_id: Mapped[int] = mapped_column(ForeignKey('room.id'))
    check_in: Mapped[date] = mapped_column(Date)
    check_out: Mapped[date] = mapped_column(Date)
    create_date: Mapped[date] = mapped_column(Date, default=date.today)

    hotel_bookings: Mapped[Hotel] = relationship(Hotel, back_populates='hotel_booking')
    room_bookings: Mapped[Room] = relationship(Room, back_populates='room_booking')

from movie_booking.movie import Movie
from movie_booking.customer import Customer
from movie_booking.booking_system import BookingSystem

def test_successful_booking():
    res=BookingSystem().book_ticket(Customer('John',25),Movie('The Batman',20),2)
    assert res['success']

def test_underage_customer():
    res=BookingSystem().book_ticket(Customer('Tim',10),Movie('The Batman',20),1)
    assert not res['success']

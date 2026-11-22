from movie_booking.movie import Movie
from movie_booking.customer import Customer
from movie_booking.booking_system import BookingSystem

class BookingDriver:
    def __init__(self):
        self.system=BookingSystem()
    def create_movie(self,title,seats):
        self.movie=Movie(title,seats)
    def create_customer(self,name,age):
        self.customer=Customer(name,age)
    def book_tickets(self,count):
        self.result=self.system.book_ticket(self.customer,self.movie,count)
        return self.result

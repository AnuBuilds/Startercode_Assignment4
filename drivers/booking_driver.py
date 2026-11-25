
from movie_booking.movie import Movie
from movie_booking.customer import Customer
from movie_booking.booking_system import BookingSystem


class BookingDriver:
    """Application driver for automated acceptance testing."""

    def __init__(self):
        self.system = BookingSystem()
        self.movie = None
        self.customer = None
        self.result = None

    def create_movie(self, title, seats):
        """Given a movie with available seats."""
        self.movie = Movie(title, seats)

    def create_customer(self, name, age):
        """Given a customer of a specified age."""
        self.customer = Customer(name, age)

    def book_tickets(self, count):
        """When the customer attempts to book tickets."""
        self.result = self.system.book_ticket(
            self.customer,
            self.movie,
            count
        )
        return self.result

    def booking_succeeded(self):
        """Check whether the booking was successful."""
        return self.result["success"]

    def booking_failed(self):
        """Check whether the booking was rejected."""
        return not self.result["success"]

    def get_booking_message(self):
        """Return the booking outcome message."""
        return self.result["message"]

    def get_available_seats(self):
        """Return the remaining available seats."""
        return self.movie.available_seats

    def get_booked_tickets(self):
        """Return the number of successfully booked tickets."""
        return self.result.get("tickets", 0)

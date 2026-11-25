
from movie_booking.booking_system import BookingSystem
from movie_booking.customer import Customer
from movie_booking.movie import Movie


def main():
    print("=== Movie Ticket Booking System ===")

    movie = Movie("The Batman", 20)
    customer = Customer("John", 25)
    booking_system = BookingSystem()

    print(f"Movie: {movie.title}")
    print(f"Customer: {customer.name}")
    print(f"Customer age: {customer.age}")
    print(f"Initial available seats: {movie.available_seats}")
    print("Requested tickets: 2")

    result = booking_system.book_ticket(customer, movie, 2)

    print(f"Booking result: {result['message']}")
    print(f"Remaining available seats: {movie.available_seats}")

    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())


from drivers.booking_driver import BookingDriver


def test_successful_booking():
    # Given
    driver = BookingDriver()
    driver.create_movie("The Batman", 20)
    driver.create_customer("John", 25)

    # When
    driver.book_tickets(2)

    # Then
    assert driver.booking_succeeded()
    assert driver.get_booking_message() == "Booking successful"
    assert driver.get_booked_tickets() == 2
    assert driver.get_available_seats() == 18


def test_minimum_age_and_exact_seat_availability():
    # Given
    driver = BookingDriver()
    driver.create_movie("The Batman", 5)
    driver.create_customer("Alex", 13)

    # When
    driver.book_tickets(5)

    # Then
    assert driver.booking_succeeded()
    assert driver.get_booked_tickets() == 5
    assert driver.get_available_seats() == 0


def test_underage_customer():
    # Given
    driver = BookingDriver()
    driver.create_movie("The Batman", 20)
    driver.create_customer("Tim", 12)

    # When
    driver.book_tickets(2)

    # Then
    assert driver.booking_failed()
    assert driver.get_booking_message() == (
        "Customer does not meet age requirement"
    )
    assert driver.get_available_seats() == 20


def test_zero_ticket_quantity():
    # Given
    driver = BookingDriver()
    driver.create_movie("The Batman", 20)
    driver.create_customer("John", 25)

    # When
    driver.book_tickets(0)

    # Then
    assert driver.booking_failed()
    assert driver.get_booking_message() == "Invalid ticket quantity"
    assert driver.get_available_seats() == 20


def test_negative_ticket_quantity():
    # Given
    driver = BookingDriver()
    driver.create_movie("The Batman", 20)
    driver.create_customer("John", 25)

    # When
    driver.book_tickets(-2)

    # Then
    assert driver.booking_failed()
    assert driver.get_booking_message() == "Invalid ticket quantity"
    assert driver.get_available_seats() == 20


def test_insufficient_available_seats():
    # Given
    driver = BookingDriver()
    driver.create_movie("The Batman", 3)
    driver.create_customer("John", 25)

    # When
    driver.book_tickets(4)

    # Then
    assert driver.booking_failed()
    assert driver.get_booking_message() == (
        "Not enough seats available"
    )
    assert driver.get_available_seats() == 3


def test_sold_out_movie():
    # Given
    driver = BookingDriver()
    driver.create_movie("The Batman", 0)
    driver.create_customer("John", 25)

    # When
    driver.book_tickets(1)

    # Then
    assert driver.booking_failed()
    assert driver.get_booking_message() == "Movie sold out"
    assert driver.get_available_seats() == 0


def test_multiple_successful_bookings():
    # Given
    driver = BookingDriver()
    driver.create_movie("The Batman", 10)
    driver.create_customer("John", 25)

    # When
    driver.book_tickets(3)
    first_booking_success = driver.booking_succeeded()
    first_remaining_seats = driver.get_available_seats()

    driver.book_tickets(2)

    # Then
    assert first_booking_success
    assert first_remaining_seats == 7
    assert driver.booking_succeeded()
    assert driver.get_booked_tickets() == 2
    assert driver.get_available_seats() == 5

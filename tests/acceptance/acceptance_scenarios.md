Feature: Movie Ticket Booking
Scenario: Successful booking
Given a movie has 20 seats
And a customer is 25 years old
When 2 tickets are booked
Then booking succeeds

Scenario: Underage customer
Scenario: Invalid ticket quantity
Scenario: Insufficient seats
Scenario: Sold out movie

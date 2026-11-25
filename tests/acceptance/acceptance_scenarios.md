
# Feature: Movie Ticket Booking

## Scenario 1: Successful booking

Given a movie has 20 available seats
And a customer is 25 years old
When the customer books 2 tickets
Then the booking is successful
And 18 seats remain available

## Scenario 2: Minimum eligible age and exact seat availability

Given a movie has 5 available seats
And a customer is exactly 13 years old
When the customer books 5 tickets
Then the booking is successful
And 0 seats remain available

## Scenario 3: Underage customer

Given a movie has 20 available seats
And a customer is 12 years old
When the customer attempts to book 2 tickets
Then the booking is rejected
And the message is "Customer does not meet age requirement"
And 20 seats remain available

## Scenario 4: Zero ticket quantity

Given a movie has 20 available seats
And a customer is 25 years old
When the customer attempts to book 0 tickets
Then the booking is rejected
And the message is "Invalid ticket quantity"
And 20 seats remain available

## Scenario 5: Negative ticket quantity

Given a movie has 20 available seats
And a customer is 25 years old
When the customer attempts to book -2 tickets
Then the booking is rejected
And the message is "Invalid ticket quantity"
And 20 seats remain available

## Scenario 6: Insufficient available seats

Given a movie has 3 available seats
And a customer is 25 years old
When the customer attempts to book 4 tickets
Then the booking is rejected
And the message is "Not enough seats available"
And 3 seats remain available

## Scenario 7: Sold-out movie

Given a movie has 0 available seats
And a customer is 25 years old
When the customer attempts to book 1 ticket
Then the booking is rejected
And the message is "Movie sold out"
And 0 seats remain available

## Scenario 8: Multiple successful bookings

Given a movie has 10 available seats
And a customer is 25 years old
When the customer books 3 tickets
And subsequently books 2 more tickets
Then both bookings are successful
And 5 seats remain available

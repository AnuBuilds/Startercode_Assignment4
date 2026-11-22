class BookingSystem:
    def book_ticket(self,customer,movie,tickets):
        if customer.age < 13:
            return {'success':False,'message':'Customer does not meet age requirement'}
        if tickets <= 0:
            return {'success':False,'message':'Invalid ticket quantity'}
        if movie.available_seats == 0:
            return {'success':False,'message':'Movie sold out'}
        if movie.available_seats < tickets:
            return {'success':False,'message':'Not enough seats available'}
        movie.available_seats -= tickets
        return {'success':True,'message':'Booking successful','tickets':tickets}

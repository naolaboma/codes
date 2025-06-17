# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:
    def __init__(self, n):
        self.marker = 1
        self.available_seats = SortedSet()
    def reserve(self):
        if self.available_seats:
            seat_number = self.available_seats.pop(0)
            return seat_number
        seat_number = self.marker
        self.marker += 1
        return seat_number
    def unreserve(self, seat_number):
        self.available_seats.add(seat_number)
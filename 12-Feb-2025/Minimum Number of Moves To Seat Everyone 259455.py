# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()

        total_moves = 0
        for i in range(len(seats)):
            total_moves += abs(seats[i] - students[i])
        
        return total_moves
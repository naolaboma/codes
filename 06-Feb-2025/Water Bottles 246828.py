# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        num_drank =0

        while(numBottles >= numExchange):
            numBottles -= numExchange
            numBottles += 1
            num_drank += numExchange
        num_drank += numBottles

        return num_drank
        
        
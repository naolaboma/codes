# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost): return -1

        res = 0
        cur = 0
        for n in range(len(gas)):
            cur+=gas[n]-cost[n]
            if cur<0:
                cur= 0
                res = n+1
                
        return res
        
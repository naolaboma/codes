# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        so = sorted(costs, key=lambda x: x[1] - x[0])
        res = 0
        for i in range(len(so)):
            if i >= (len(so)//2):
                res+= so[i][0]
            else:
                res+=so[i][1]
        return res
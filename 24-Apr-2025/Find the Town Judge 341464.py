# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        ind = [0] * (N + 1)
        otd = [0] * (N + 1)
        for a in trust:
            otd[a[0]] += 1
            ind[a[1]] += 1
        for i in range(1, N + 1):
            if ind[i] == N - 1 and otd[i] == 0:
                return i
        return -1
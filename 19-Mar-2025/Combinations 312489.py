# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        p = []
        def combin(s,p):
            if len(p) == k:
                result.append(list(p))
                return
            for i in range(s, n+1):
                p.append(i)
                combin(i+1, p)
                p.pop()
        result = []
        combin(1,p)
        return result
# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = [x for x in range(1,n+1)]
        return list(combinations(stack,k))
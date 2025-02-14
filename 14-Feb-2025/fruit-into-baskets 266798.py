# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r, maxs = 0, 0, 0
        c = defaultdict(int)
        k = 2
        while r < len(fruits):
            c[fruits[r]] += 1
            while len(c) > k:
                c[fruits[l]] -= 1
                if c[fruits[l]] == 0:
                    c.pop(fruits[l])
                l += 1
            maxs = max(maxs, r - l + 1)
            r += 1
        return maxs
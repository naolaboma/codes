# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c1 = Counter(answers)
        res = 0
        for k, v in c1.items():
            ss = k + 1
            num = ceil(v / ss)
            res += num * ss
        return res
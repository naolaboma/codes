# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        c = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i]*nums[j]
                c[product]+=1
        res = 0
        for v in c.values():
            p = (v*(v-1))//2
            res += 8*p
        return res
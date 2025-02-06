# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res1 = []
        res2 = []
        for i in range(len(nums)):
            if i + 1 <= len(nums):
                if nums[i-1] == nums[i]:
                    nums[i-1]*=2
                    nums[i]=0
        r1=[]
        r2=[]
        for v in nums:
            if v!=0:
                r1.append(v)
            else:
                r2.append(v)
        r = r1+r2
        return r
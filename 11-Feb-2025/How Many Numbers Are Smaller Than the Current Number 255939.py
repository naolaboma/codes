# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out=[]
        for i in range(len(nums)):
            res = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    res+=1
            out.append(res)
        return out
# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result=[]
        for i in range(n):
            if nums[i] > 0:
                i = i + nums[i]
                i = i%n
                result.append(nums[i])
            elif nums[i] < 0:
                i -= abs(nums[i])
                i = i%n
                result.append(nums[i])
                continue
            else:
                result.append(nums[i])
            
        return result
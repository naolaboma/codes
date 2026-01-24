class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        maxi = float('-inf')
        while l<r:
            summ = nums[l]+nums[r]
            maxi = max(maxi, summ)
            l+=1
            r-=1
        return maxi

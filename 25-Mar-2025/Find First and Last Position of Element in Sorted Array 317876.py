# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0 ,len(nums)-1
        res = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] != target and res == target:
                break
            if nums[mid] == target:
                res = mid
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        res2 = -1
        l,r = 0 ,len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] != target and res2 == target:
                break
            if nums[mid] == target:
                res2 = mid
                l = mid+1
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
            
        return [res, res2]
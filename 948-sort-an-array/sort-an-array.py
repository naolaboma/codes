class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = [0] * len(nums)
        self.mergesort(nums,temp, 0, len(nums)-1)
        return nums
    def merge(self, nums, temp, lb, mid, ub):
        i = lb
        j = mid + 1
        k = lb
        while i <= mid and j <= ub:
            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                i+=1
            else:
                temp[k] = nums[j]
                j+=1
            k+=1
        if i > mid:
            while j <= ub:
                temp[k] = nums[j]
                j+=1
                k+=1
        else:
            while i <= mid:
                temp[k] = nums[i]
                i+=1
                k+=1
        for x in range(lb, ub+1):
            nums[x] = temp[x]
    def mergesort(self, nums, temp, lb, ub):
        if lb < ub:
            mid = (lb + ub)//2
            self.mergesort(nums, temp, lb, mid)
            self.mergesort(nums, temp, mid+1, ub)
            self.merge(nums, temp, lb, mid, ub)
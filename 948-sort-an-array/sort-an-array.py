class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.heapsort(nums, len(nums))
        return nums
    def maxheapify(self, nums, n, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n and nums[l] > nums[largest]:
            largest = l
        if r < n and nums[r] > nums[largest]:
            largest = r
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.maxheapify(nums, n, largest)
    def heapsort(self, nums, n):
        for i in range(n//2-1, -1, -1):
            self.maxheapify(nums, n, i)
        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.maxheapify(nums, i, 0)

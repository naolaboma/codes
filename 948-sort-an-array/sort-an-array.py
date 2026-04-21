class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #counting sort
        mini = min(nums)
        maxi = max(nums)
        count = [0] * ((maxi - mini) + 1)
        for num in nums:
            count[num - mini] +=1
        idx = 0
        for i, freq in enumerate(count):
            while freq > 0:
                nums[idx] = i + mini
                idx += 1
                freq -= 1
        return nums
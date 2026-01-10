class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        res = Counter(nums)
        for key, value in res.items():
            if value >= 2:
                return key
        
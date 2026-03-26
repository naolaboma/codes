class Solution:
    def search(self, nums: List[int], target: int) -> int:
        so = sorted(list(enumerate(nums)))
        for i, v in so:
            if v == target:
                return i
        return -1
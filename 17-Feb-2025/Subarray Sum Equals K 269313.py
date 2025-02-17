# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        p = 0
        freq = {0: 1}
        for num in nums:
            p += num
            if p - k in freq:
                count += freq[p - k]
            if p in freq:
                freq[p] += 1
            else:
                freq[p] = 1
        return count
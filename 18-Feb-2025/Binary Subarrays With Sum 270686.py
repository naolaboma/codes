# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ps = 0
        freq = {0:1}
        count = 0
        for num  in nums:
            ps +=num
            if ps - goal in freq:
                count+= freq[ps-goal]
            if ps in freq:
                freq[ps]+=1
            else:
                freq[ps] = 1
        return count
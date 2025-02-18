# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        totalsumm = 0
        freq ={0:1}
        for num in nums:
            totalsumm += num
            if totalsumm%k in freq:
                count+=freq[totalsumm%k]
            if totalsumm%k in freq:
                freq[totalsumm%k]+=1
            else:
                freq[totalsumm%k]=1
        return count
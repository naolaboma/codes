# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c1 = Counter(nums)
        p=0
        un_p=0
        print(c1)
        for k,v in c1.items():
            p +=v//2
            un_p += v % 2
        return [p, un_p]
# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1, xor2 = 0, 0
        len1, len2 = len(nums1), len(nums2)
        if len2 % 2:
            for num in nums1:
                xor1 ^= num
        if len1 % 2:
            for num in nums2:
                xor2 ^= num
        return xor1 ^ xor2
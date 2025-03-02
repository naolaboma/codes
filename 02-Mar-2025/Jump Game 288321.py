# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        win = n - 1  
        if n == 1:
            return True  
        for i in range(n - 2, -1, -1):
            if win - i <= nums[i]:
                win = i   
        return win == 0
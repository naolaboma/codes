# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        ans = float('inf')
        min_distance = float('inf')
        for i in range(N-2):
            left = i+1
            right = N-1
            while (left < right):
                s = nums[i] + nums[left]+nums[right]
                dis = abs(s-target)
                if dis < min_distance:
                    min_distance = dis
                    ans = s

                if s < target:
                    left+=1
                else:
                    right-=1
            
        return ans
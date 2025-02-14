# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for idx1 in range(len(nums) - 2):
            if idx1 > 0 and nums[idx1] == nums[idx1 - 1]:
                continue  
            if nums[idx1] > 0:
                break
            num = -nums[idx1]
            idx2, idx3 = idx1 + 1, len(nums) - 1
            while idx2 < idx3:
                if nums[idx2] + nums[idx3] == num:
                    result.add((nums[idx1], nums[idx2], nums[idx3]))
                    idx2 += 1
                    idx3 -= 1
                    while idx2 < idx3 and nums[idx2] == nums[idx2 - 1]:
                        idx2 += 1
                    while idx2 < idx3 and nums[idx3] == nums[idx3 + 1]:
                        idx3 -= 1
                elif  nums[idx2] + nums[idx3] < num:
                    idx2 += 1
                else:
                    idx3 -= 1
        return [list(arr) for arr in list(result)]
        
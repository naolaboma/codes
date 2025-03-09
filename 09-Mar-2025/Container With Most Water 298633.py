# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        res = []
        while l<r:
            vol = (r-l) *(min(height[r],height[l]))
            res.append(vol)
            if height[l] < height[r]:
                
                l+=1
            else:
                r-=1
        return max(res)
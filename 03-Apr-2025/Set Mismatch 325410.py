# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        se = set(nums)
        def getcount(c):
            for k, v in c.items():
                if v==2 :
                    return k

        def getmissing(se, n):
            for i in range(1, n+1):
                if i not in se:
                    return i 
        return [getcount(c), getmissing(se, len(nums))]
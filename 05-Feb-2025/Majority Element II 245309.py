# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        c = defaultdict(int)
        for x in nums:
            c[x]+=1
        output=[]
        for ke, v in c.items():
            if v > (n//3):
                output.append(ke)
        return output
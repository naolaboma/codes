class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        leftsumm = 0
        rightsumm = sum(nums)
        count = 0
        for x in nums:
            leftsumm += x
            rightsumm -= x
            if (leftsumm-rightsumm)%2 == 0 and rightsumm!=0:
                count +=1
        return count

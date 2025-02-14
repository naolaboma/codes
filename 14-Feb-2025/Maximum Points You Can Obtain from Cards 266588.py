# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum, rsum,maxsum = 0,0,0
        for i in range(k):
            lsum+=cardPoints[i]
        maxsum = lsum
        rind = len(cardPoints)-1
        for i in range(k-1,-1,-1):
            lsum -= cardPoints[i]
            rsum += cardPoints[rind]
            maxsum = max(maxsum, lsum+rsum)
            rind-=1
        return maxsum
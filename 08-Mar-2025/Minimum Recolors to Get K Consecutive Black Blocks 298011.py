# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        blocks = list(blocks)
        l,r = 0,k
        mini = float('inf')
        while r <= len(blocks):
            res = blocks[l:r]
            cw = res.count('W')
            mini = min(mini, cw)
            l+=1
            r+=1
        return mini

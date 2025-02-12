# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c1 = defaultdict(str)
        for i in range(len(s)):
            c1[s[i]]=i
        size,end = 0,0
        res = []
        for i in range(len(s)):
            size+=1
            end = max(end,c1.get(s[i]))
            if i == end:
                res.append(size)
                size = 0
        return res
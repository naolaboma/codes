# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = list(map(str, nums))
        c1 = defaultdict(list)
        for k in res:
            c1[int(k[0])].append(k)
        sortd = dict(sorted(c1.items(), key=lambda item: item[0], reverse=True))
        res1 = []
        for group in sortd.values():
            res1.append(sorted(group, key=lambda x: x*10, reverse=True))
        res2 = ""
        for l in res1:
            for m in l:
                res2 += m 
        return res2 if res2[0] != '0' else '0'
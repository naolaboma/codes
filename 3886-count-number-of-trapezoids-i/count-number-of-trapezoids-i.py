class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        pnum = defaultdict(int)
        mod = 10**9 +7
        ans, total = 0, 0
        for p in points:
            pnum[p[1]]+=1
        for p_n in pnum.values():
            edge = p_n*(p_n -1)//2
            ans = (ans + edge * total) % mod
            total = (total + edge) % mod
        return ans
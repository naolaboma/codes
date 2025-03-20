# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        p = [0]*k
        self.mi = float('inf')
        def distr(s):
            if s == len(cookies):
                self.mi = min(self.mi, max(p))
                return
            for i in range(k):
                p[i] += cookies[s]
                distr(s+1)
                p[i] -= cookies[s]
                if p[i]==0:
                    break
        distr(0)
        return self.mi
        
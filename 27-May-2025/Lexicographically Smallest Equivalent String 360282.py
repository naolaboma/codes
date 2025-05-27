# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        UF = {}
        def find(x):
            UF.setdefault(x,x)
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX>rootY:
                UF[rootX] = rootY
            else:
                UF[rootY] = rootX
        for i in range(len(s1)):
            union(s1[i],s2[i])
        res = []
        for c in baseStr:
            res.append(find(c))   
        return ''.join(res)
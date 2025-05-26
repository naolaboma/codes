# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indeg = [0]*n
        for u, v in edges:
            indeg[v]+=1
        champ = -1
        champcount = 0
        for i in range(len(indeg)):
            if indeg[i]== 0:
                champcount+=1
                champ = i
        if champcount>1:
            return -1
        else:
            return champ
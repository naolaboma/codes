# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n,m = len(firstList), len(secondList)
        i,j = 0,0
        ps = []
        while i<n and j<m:
            lft = max(firstList[i][0], secondList[j][0])
            rt = min(firstList[i][1], secondList[j][1])
            if lft <= rt :
                ps.append([lft,rt])
            if firstList[i][1] < secondList[j][1]:
                i+=1
            else:
                j+=1
        return ps
# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        ranges = (max(heights)-min(heights))
        res = [0]*(ranges+1)
        for i in range(len(heights)):
            res[heights[i]-max(heights)-1]=names[i]
        name = []
        for k in res:
            if k!=0:
                name.append(k)
        return name[::-1]
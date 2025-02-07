# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ro = len(matrix)
        co = len(matrix[0])
        l, t, r, b = 0,0,co,ro
        output =[]
        while l < r and t<b:
            for i in range(l,r):
                output.append(matrix[t][i])
            t+=1
            for i in range(t,b):
                output.append(matrix[i][r-1])
            r-=1
            if not(l < r and t<b):
                break
            for i in range(r-1,l-1,-1):
                output.append(matrix[b-1][i])
            b-=1
            for i in range(b-1,t-1,-1):
                output.append(matrix[i][l])
            l+=1
        return output
            
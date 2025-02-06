# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, column = len(img), len(img[0])
        res = [[0]*column for k in range(len(img))]
        for r in range(rows):
            for c in range(column):
                total,cnt =0, 0
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if i <0 or i == rows or j<0 or j==column:
                            continue
                        total+=img[i][j]
                        cnt+=1
                res[r][c] = total//cnt
        return res
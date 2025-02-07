# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            for j in range(n):
                if image[i][j] == 0:
                    image[i][j] = 1
                elif image[i][j] ==1:
                    image[i][j]=0
        re = []
        for k in image:
            re.append(k[::-1])
        return re
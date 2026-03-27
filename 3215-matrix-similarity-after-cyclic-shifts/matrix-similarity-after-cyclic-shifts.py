class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        mini = mat.copy()
        n = len(mat)
        p = len(mat[0])
        for i in range(k%p):
            for j in range(n):
                if j%2 == 0:
                    mat[j] = mat[j][1:] + mat[j][:1]
                else:
                    mat[j] = mat[j][p-1:] + mat[j][:p-1]
        return mini == mat
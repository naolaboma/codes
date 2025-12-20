class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        k = len(strs[0])
        count = 0
        for j in range(k):
            for i in range(1, n):
                if strs[i][j]< strs[i-1][j]:
                    count +=1
                    break
        return count
            
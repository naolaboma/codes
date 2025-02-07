# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        r = []
        for k in s:
            r.append(list(k))
        col = []
        for l in r:
            col.append(len(l))
        column = max(col)
        rows, colm = column, len(r)
        ins = [[" "]*colm for h in range(rows)]
        for i in range(colm):
            for j in range(len(r[i])):
                ins[j][i] = r[i][j]
        ans = []
        for k in ins:
            ans.append("".join(k).rstrip())
        return ans
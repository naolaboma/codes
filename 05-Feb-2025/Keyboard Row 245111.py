# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"),set("asdfghjkl"), set("zxcvbnm")]
        ans = []
        for s in words:
            for x in rows:
                if all(c in x for c in s.lower()):
                    ans.append(s)
                    break
        return ans
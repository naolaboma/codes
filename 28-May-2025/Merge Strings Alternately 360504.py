# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        st=[]
        while len(word1)>i or len(word2)>i:
            if len(word1)>i:
                st.append(word1[i])
            if len(word2)>i:
                st.append(word2[i])
            i+=1     
        return ''.join(st)
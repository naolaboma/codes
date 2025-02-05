# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        c1 = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    c1[list1[i]] = i+j
        print(c1)
        res=[]
        for k, v in c1.items():
            if v == min(c1.values()):
                res.append(k)
        return res
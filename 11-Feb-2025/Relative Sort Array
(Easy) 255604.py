# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        nonin= []
        for i in range(len(arr2)):
            ress = []
            for j in range(len(arr1)):
                if arr1[j]==arr2[i]:
                    ress.append(arr1[j])
            res.extend(ress)
        r = []
        for k in arr1:
            if k not in res:
                r.append(k)
        r.sort()
        print(r)
        res= res+r
        return res
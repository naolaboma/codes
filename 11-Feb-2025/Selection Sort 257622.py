# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        for i in range(n):
            mi = i
            for j in range(i+1,n):
                if arr[mi]>arr[j]:
                    mi = j
            arr[i],arr[mi] = arr[mi],arr[i]
        return arr
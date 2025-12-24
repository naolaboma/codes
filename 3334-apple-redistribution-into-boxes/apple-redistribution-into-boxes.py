class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)

        summapple = sum(apple)
        count = 0
        for x in capacity:
            if summapple > 0:
                summapple-=x
                count +=1
            else:
                break
        return count

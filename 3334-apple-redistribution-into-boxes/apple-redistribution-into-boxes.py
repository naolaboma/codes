class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)

        summapple = sum(apple)
        count = 0
        print(capacity)
        for x in capacity:
            if summapple > 0:
                count +=1
            summapple-=x
        return count

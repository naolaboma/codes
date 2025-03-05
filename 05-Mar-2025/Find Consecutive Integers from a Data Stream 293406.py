# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.v = value
        self.k = k
        self.n = 0
    def consec(self, num: int) -> bool:
        if num == self.v:
            self.n += 1
        else:
            self.n = 0
        return self.n >= self.k
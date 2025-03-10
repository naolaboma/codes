# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:
    def __init__(self):
        self.que = deque()
        self.leng = 0
    def push(self, x: int) -> None:
        self.que.append(x)
        self.leng+=1
    def pop(self) -> int:
        self.c = self.que.pop()
        self.leng-=1
        return self.c
    def top(self) -> int:
        return self.que[-1]
    def empty(self) -> bool:
        return self.leng == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
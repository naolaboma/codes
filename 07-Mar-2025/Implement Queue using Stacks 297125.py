# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.queue = []
        self.n = len(self.queue)

    def push(self, x: int) -> None:
        self.queue = [x] + self.queue
        self.n+=1
    def pop(self) -> int:
        self.ou = self.queue[self.n-1]
        self.queue = self.queue[:self.n-1]
        self.n-=1
        return self.ou
    def peek(self) -> int:
        return self.queue[self.n-1]
    def empty(self) -> bool:
        return self.n == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:
    def __init__(self):
        self.data = []
        self.index_map = {}
    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.data.append(val)
        self.index_map[val] = len(self.data) - 1
        return True
    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        idx_to_remove = self.index_map[val]
        last_val = self.data[-1] 
        self.data[idx_to_remove] = last_val
        self.index_map[last_val] = idx_to_remove
        self.data.pop()
        del self.index_map[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.data) 
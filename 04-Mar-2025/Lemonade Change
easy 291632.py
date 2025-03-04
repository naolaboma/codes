# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c1 = defaultdict(int)
        for income in bills:
            if income == 5:
                c1[5] += 1

            elif income == 10:
                if c1[5] > 0:
                    c1[5] -= 1
                    c1[10] += 1
                else:
                    return False  
            else: 
                if c1[10] > 0 and c1[5] > 0:
                    c1[10] -= 1
                    c1[5] -= 1
                elif c1[5] >= 3:  
                    c1[5] -= 3
                else:
                    return False  
        return True
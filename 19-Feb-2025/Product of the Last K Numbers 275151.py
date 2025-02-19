# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:
    def __init__(self):
        self.res = [1]
        self.lenn = 1
    def add(self, num: int) -> None:
        if num == 0:
            self.res = [1]
            self.lenn = 1
        else:
            self.res.append(self.res[-1]*num)
            self.lenn+=1
    def getProduct(self, k: int) -> int:
        ind = self.lenn -k -1
        if ind < 0:
            return 0
        return self.res[-1] // self.res[ind]
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
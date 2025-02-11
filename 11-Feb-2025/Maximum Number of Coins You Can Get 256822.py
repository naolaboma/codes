# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        pile = sorted(piles, reverse = True)
        print(pile)
        n = len(piles)
        mine = 0
        hers = 0
        bob = 0
        for i in range(len(pile)//3):
            hers += pile[0]
            pile.remove(pile[0])

            mine += pile[0]
            pile.remove(pile[0])

            bob+=piles[0]
            piles.remove(piles[0])
        return mine
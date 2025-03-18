# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        que = deque(range(len(deck)))
        res = [0] * len(deck)
        for card in deck:
            res[que.popleft()] = card
            if que:
                que.append(que.popleft())
        return res
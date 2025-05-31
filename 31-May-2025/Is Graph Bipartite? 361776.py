# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def validColouring(self, gr, colour, node, col):
        if colour[node] != 0:
            return colour[node] == col
        colour[node] = col
        for ne in gr[node]:
            if not self.validColouring(gr, colour, ne, -col):
                return False
        return True
    def isBipartite(self, gr):
        n = len(gr)
        colour = [0] * n
        for node in range(n):
            if colour[node] == 0 and not self.validColouring(gr, colour, node, 1):
                return False
        return True
class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))
        min_time = [inf] * n
        min_time[0] = 0
        heap = [(0, 0)] 
        while heap:
            curr_time, node = heappop(heap)
            if node == n-1:
                return curr_time
            if curr_time == min_time[node]:
                for neighbor, w in graph[node]:
                    new_time = curr_time + w
                    if min_time[neighbor] > new_time:
                        min_time[neighbor] = new_time
                        heappush(heap, (new_time, neighbor))
        return -1  
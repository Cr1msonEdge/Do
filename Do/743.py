import heapq
from typing import defaultdict, List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # k - стартовая вершиан
        hp = [[0, k]]
        heapq.heapify(hp)
        visited_nodes = set()
        graph = defaultdict(list)

        for time in times:
            graph[time[0]].append([time[1], time[2]])
        
        while hp:
            # heappop берет минимальный по первому элементу из пары
            weight, node = heapq.heappop(hp)
            if node in visited_nodes:
                continue
            visited_nodes.add(node)
            
            if len(visited_nodes) == n:
                return weight

            for nd, w in graph[node]:
                heapq.heappush(hp, [w + weight, nd])

        return -1



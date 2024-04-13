from typing import List
from collections import defaultdict


def dfs_cycle(startNode: int, graph: defaultdict, visitedList: List, on_observe: List):
    visitedList[startNode] = True
    on_observe[startNode] = True

    for node in graph[startNode]:
        if not visitedList[node]:
            if dfs_cycle(node, graph, visitedList, on_observe):
                return True
        elif visitedList[node] and on_observe[node]:
            return True

    on_observe[startNode] = False
    return False


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # список смежности
    graph = defaultdict(set)

    visited = [False for _ in range(numCourses)]
    straight_edge = [False for _ in range(numCourses)]
    for node in prerequisites:
        graph[node[1]].add(node[0])

    for node in prerequisites:
        if not (visited[node[1]]) and dfs_cycle(node[1], graph, visited, straight_edge):
            return False

    return True




print(canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))

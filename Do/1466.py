class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        result = [0]

        def dfs(graph, visited_nodes, start_node):
            visited_nodes[start_node] = True
            for node in graph[start_node]:
                if node >= 0:
                    if not visited_nodes[node]:
                        dfs(graph, visited_nodes, node)
                else:
                    node *= -1
                    if not visited_nodes[node]:
                        result[0] += 1
                        dfs(graph, visited_nodes, node)

        sz = len(connections)
        visited_nodes = []
        graph = []
        for _ in range(n):
            visited_nodes.append(False)
            graph.append([])
        for i in range(sz):
            graph[connections[i][1]].append(connections[i][0])
            graph[connections[i][0]].append(-connections[i][1])
        dfs(graph, visited_nodes, 0)

        return result[0]
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        sz = len(graph) - 1

        def find_path(curr_nodes, path):
            if path[-1] == sz:
                result.append(path)
                return
            for node in curr_nodes:
                find_path(graph[node], path + [node])

        find_path(graph[0], [0])
        return result
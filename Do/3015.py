from typing import List


def Floyd_Warshall(n: int, matrix: List[List[float]]) -> List[List[float]]:
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (matrix[j][i] + matrix[i][k]) < matrix[j][k]:
                    matrix[j][k] = matrix[j][i] + matrix[i][k]
    return matrix

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        x -= 1
        y -= 1
        graph = [[1e10 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1):
            graph[i][i + 1] = 1
            graph[i + 1][i] = 1

        graph[x][y] = graph[y][x] = 1

        graph = Floyd_Warshall(n, graph)

        result = [0 for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if graph[i][j] < n:
                    result[int(graph[i][j] - 1)] += 2

        return result
        
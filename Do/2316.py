from typing import List

def NumberOfPairsForN(N: int):
    return N * (N - 1) / 2



class UnionJoint:
    link = []
    size = []

    def __init__(self, n: int):
        self.link = []
        self.size = []
        for i in range(n):
            self.link.append(i)
            self.size.append(1)

    def find(self, x: int) -> int:
        if x == self.link[x]:
            return x
        self.link[x] = self.find(self.link[x])
        return self.link[x]

    def unite(self, a: int, b: int):
        a = self.find(a)
        b = self.find(b)
        if self.size[a - 1] < self.size[b - 1]:
            a, b = b, a
        self.size[a] += self.size[b]
        self.link[b] = a

    def same(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)




class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        union_joint_graph = UnionJoint(n)
        for edge in edges:
            parent_a = union_joint_graph.find(edge[0])
            parent_b = union_joint_graph.find(edge[1])
            if parent_a != parent_b:
                union_joint_graph.unite(edge[0], edge[1])

        print(union_joint_graph.link)
        print('-------')
        print(union_joint_graph.size)
        # случай, если нет ребёр
        N = NumberOfPairsForN(n)
        if len(edges) == 0:
            return int(N)

        result = 0
        for i in range(len(union_joint_graph.link)):
            if union_joint_graph.find(i) == i:
                result += NumberOfPairsForN(union_joint_graph.size[i])
        print(result)
        return int(N - result)
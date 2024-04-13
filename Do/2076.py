from typing import List


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
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        result = [True for _ in range(len(requests))]
        union_joint_graph = UnionJoint(n)
        for index, nodes in enumerate(requests):
            a = nodes[0]
            b = nodes[1]
            parent_a = union_joint_graph.find(a)
            parent_b = union_joint_graph.find(b)
            for i, j in restrictions:
                parent_i = union_joint_graph.find(i)
                parent_j = union_joint_graph.find(j)
                if (parent_a == parent_i and parent_b == parent_j) or (parent_a == parent_j and parent_b == parent_i):
                    result[index] = False
                    break

            if result[index]:
                union_joint_graph.unite(a, b)
        return result
        
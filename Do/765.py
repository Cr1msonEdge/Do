from typing import List


class UnionJoint:
    link = []
    size = []
    count = 0
    
    def __init__(self, n: int):
        self.link = []
        self.size = []
        self.count = n
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
        if a == b:
            return
        if self.size[a - 1] < self.size[b - 1]:
            a, b = b, a
        self.size[a] += self.size[b]
        self.link[b] = a
        self.count -= 1
        
    def same(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        sz = len(row) // 2
        union_joint_graph = UnionJoint(sz)
        for i in range(sz):
            first_group = row[2 * i] // 2
            second_group = row[2 * i + 1] // 2
            union_joint_graph.unite(first_group, second_group)
        return sz - union_joint_graph.count
        
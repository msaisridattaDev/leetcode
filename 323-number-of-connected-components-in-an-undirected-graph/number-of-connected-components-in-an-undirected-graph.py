class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        # path compression: When finding the root r of the tree containing x,
        # change the parent pointer of all nodes along the path to point directly to r
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Maintain an integer rank for each node, initially 0. Link root of
        # smaller rank to root of larger rank; if tie, increase rank of larger root by 1.
        px, py = self.find(x), self.find(y)
        # if they were already connected, do nothing and return 0
        if px == py:
            return 0
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank[py] += 1
        # return 1 if performed union
        return 1
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = n
        for x, y in edges:
            res -= uf.union(x, y)
        return res
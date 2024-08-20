class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        queue = deque()
        color = [-1]*len(graph)
        for i in range(len(graph)):
            if color[i] == -1:
                queue.append((i,0))
                color[i] = 0
                while queue:
                    u,c = queue.popleft()
                    for v in graph[u]:
                        if color[v] == -1:
                            color[v] = 1-c
                            queue.append((v,1-c))
                        else:
                            if color[v] == c:
                                return False
        return True
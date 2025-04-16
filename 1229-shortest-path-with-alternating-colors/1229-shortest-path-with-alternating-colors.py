class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph_blue = [[] for _ in range(n)]
        graph_red = [[] for _ in range(n)]

        for a, b in blueEdges:
            graph_blue[a].append(b)
        for a, b in redEdges:
            graph_red[a].append(b)
        queue = deque([[0, True], [0, False]])
        visited = set()
        level = 0
        result = [-1]*n
        while queue:
            
            for _ in range(len(queue)):
                node, blue = queue.popleft()
                if (node, blue) in visited:
                    continue
                result[node] = level if result[node] == -1 or result[node] > level else result[node]
                visited.add((node, blue))
                if blue:
                    for nb in graph_red[node]:
                        queue.append([nb, False])
                else:
                    for nb in graph_blue[node]:
                        queue.append([nb, True])
            level += 1
        return result  
                
        
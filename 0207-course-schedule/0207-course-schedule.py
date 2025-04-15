class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)
        color = [0]*numCourses
        def check_cycle(node):
            nonlocal result
            if color[node] == 2:
                return
            color[node] = 1
            for nb in graph[node]:
                if color[nb] == 0:
                    check_cycle(nb)
                elif color[nb] == 1:
                    result = False
            color[node] = 2
        result = True
        for i in range(numCourses):
            check_cycle(i)
        return result

        
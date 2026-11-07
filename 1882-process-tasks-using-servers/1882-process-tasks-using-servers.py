
from heapq import heapify, heappop, heappush

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        m = len(tasks)

        # Available servers: (weight, index)
        heap = [(weight, i) for i, weight in enumerate(servers)]
        heapify(heap)

        # Busy servers: (finishing_time, index)
        process = []

        def remove_free(time):
            while process and process[0][0] <= time:
                fin, index = heappop(process)
                heappush(heap, (servers[index], index))

        time = 0
        ans = [0] * m

        for i in range(m):

            # Current time cannot be earlier than task arrival
            time = max(time, i)

            # Release completed servers
            remove_free(time)

            # If all servers are busy, jump to next completion
            if not heap:
                time = process[0][0]
                remove_free(time)

            # Assign task
            weight, index = heappop(heap)
            ans[i] = index

            # Record server completion
            heappush(process, (time + tasks[i], index))

        return ans

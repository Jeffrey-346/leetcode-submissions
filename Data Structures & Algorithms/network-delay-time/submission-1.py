class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # this seems to just be shortest weighted path, use dijkstra's
        # make a heap
        # add each edge coming out of node k
        # take the smallest edge (settle the closest node)
        # add all edges/neighboring nodes from the node we just settled

        # to do this we should create a map from nodes to (neighbor, 
        # distance)

        neighbors = defaultdict(list)
        for time in times:
            neighbors[time[0] - 1].append((time[2], time[1] - 1))

        heap = []
        heapq.heappush(heap, (0, k - 1))

        dist = {}


        while heap:
            # settle the closest node
            distance, node = heapq.heappop(heap)
            if node in dist:
                continue

            dist[node] = distance

            # relax its edges
            for weight, neighbor in neighbors[node]:
                if neighbor not in dist:
                    heapq.heappush(heap, (weight + distance, neighbor))
        if len(dist) != n:
            return -1
        return max(dist.values())



        
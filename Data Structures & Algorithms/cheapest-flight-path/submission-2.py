class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # map from flight to cost
        # make adjacency list
        # breadth first search (by level) but we don't have a visited set()
        # instead we just search until we've reached k stops
        
        # initialize cost to each location as infinitely
        # while search depth < k:
        # add neighbors to frontier

        adj = [[] for i in range(n)]
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))
        
        prices = [float("inf")] * n
        prices[src] = 0
        
        queue = deque()
        queue.append(src)
        stops = 0
        while queue and stops < k + 1:
            new_queue = deque()
            old_prices = prices.copy()
            for _ in range(len(queue)):
                loc = queue.popleft()
                for neighbor, price in adj[loc]:
                    if old_prices[loc] + price < prices[neighbor]:
                        prices[neighbor] = old_prices[loc] + price
                        new_queue.append(neighbor)
            queue = new_queue
            stops += 1
        if prices[dst] == float("inf"):
            return -1
        return prices[dst]


        
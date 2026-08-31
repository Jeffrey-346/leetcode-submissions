class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # the idea is we want to not idle
        # maintain a cycles timer
        # make a tasks heap
        # track the number of each task with a dict
        # add all them to the tasks heap
        # make an empty idling heap
        # Now loop while the heap is has elms or idling heap has elms
        # (we want to complete the most common)
        # - remove as many elements as we can from idling heap and add
        #   them to tasks heap
        # - remove most freq task from the heap, decrement its number
        #   of tasks in dict
        # - if tasks are still greater than 0 add it to idling heap (min 
        #   heap) with the current cycle + n as key. 
        # - increment cycles

        cycles = 0
        remaining = defaultdict(int)
        # get the frequency (remaining number) of each task
        for task in tasks:
            remaining[task] += 1
        tasks = []
        for task in remaining:
            tasks.append((-1 * remaining[task], task))
        heapq.heapify(tasks)
        idling = []
        while tasks or idling:
            while idling and idling[0][0] <= cycles:
                cooloff, task = heapq.heappop(idling)
                heapq.heappush(tasks, (-1 * remaining[task], task))
            if tasks:
                _, task = heapq.heappop(tasks)
                remaining[task] -= 1
                if remaining[task] > 0:
                    heapq.heappush(idling, (cycles + n + 1, task))
            cycles += 1
        return cycles

        
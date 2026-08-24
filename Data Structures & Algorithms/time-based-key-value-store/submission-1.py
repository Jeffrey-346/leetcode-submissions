class TimeMap:

    def __init__(self):
        # We have a the key as the key and then a list of (values, 
        # timestamp) tuples. We can then use binary search to get
        # the correct value for the timestamp
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))
        

    # retrieve value from the closest timestamp <= timestamp
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.time_map[key]
        if len(values) == 0:
            return res
        l, r = 0, len(values) - 1 # if it's empty, then we just rtn
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] > timestamp:
                r = mid - 1
            else:
                res = values[mid][0]
                l = mid + 1

        return res
        

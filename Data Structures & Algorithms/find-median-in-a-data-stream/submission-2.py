class MedianFinder:

    def __init__(self):
        # we want to weight the number by its closeness to the middle
        # but that changes...
        self.less = [] # must be within one length of each other
        self.greater = []
        self.median = None
        

    def addNum(self, num: int) -> None:
        if not self.median or num <= self.median:
            heapq.heappush(self.less, -1*num)
        else:
            heapq.heappush(self.greater, num)
        # even out the heaps (should only need one swap per call)
        while len(self.less) < len(self.greater) - 1:
            elm = -1 * heapq.heappop(self.greater)
            heapq.heappush(self.less, elm) 

        while len(self.greater) < len(self.less) - 1:
            elm = -1 * heapq.heappop(self.less)
            heapq.heappush(self.greater, elm)

        if len(self.greater) == len(self.less):
            self.median = (-1 * self.less[0] + self.greater[0]) / 2
            return
        if len(self.greater) > len(self.less):
            self.median =  self.greater[0]
            return
        if len(self.greater) < len(self.less):
            self.median = -1 * self.less[0]
            return
            

    def findMedian(self) -> float:
        return self.median
        
        
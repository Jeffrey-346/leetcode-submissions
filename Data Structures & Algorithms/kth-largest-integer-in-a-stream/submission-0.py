class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.sort = sorted(nums)
        self.idx = len(nums) - k
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.sort = sorted(self.nums)
        self.idx = len(self.nums) - self.k
        return self.sort[self.idx]
    

        

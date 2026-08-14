class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # naive implementation
        # iterate through the list
        # keep a map from element (the integer) to its frequency
            # creating this takes O(n)
        # but how do we get the most frequent??

        # guaranteed that each int shows up a unique number of times
        # index represents frequency and the actaul entry is the int

        # for example (if we initialize array to zero)
        # [0, 1, 2, 3]
        # [0, 0, 7]

        # worst-case scenario, how big is our array?? 
        # Conservatively, can't be bigger than our input
        my_list = [[] for _ in range(len(nums) + 1)]
        my_dict = defaultdict(int)
        # create dictionary
        for num in nums:
            my_dict[num] += 1
        # fill out my_list
        for key in my_dict.keys():
            frequency = my_dict[key]
            my_list[frequency].append(key)
        res = []
        # iterate backwards until we hit a number
        for i in range(len(nums), -1, -1):
            if k == 0:
                break
            if my_list[i]:
                for elm in my_list[i]:
                    res.append(elm)
                    k -= 1
        return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list
        # go through each element
        # -> if it is the same as the last one, skip
        # -> if it is different:
        #.   -> run two sum with the correct target

        sort = sorted(nums)
        res = []

        for i in range(len(sort)):
            if i == 0 or sort[i] != sort[i - 1]:
                target = -1*sort[i]
                l, r = i + 1, len(nums) - 1
                while l < r:
                    if sort[l] + sort[r] < target:
                        l+=1
                    elif sort[l] + sort[r] > target: 
                        r-=1
                    else:
                        res.append([sort[i], sort[l], sort[r]])
                        l+=1
                        while sort[l] == sort[l - 1] and l < r:
                            l+=1
        return res

                


    
        
        
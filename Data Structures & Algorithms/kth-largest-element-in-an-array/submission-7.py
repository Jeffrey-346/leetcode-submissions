class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        def quickSort(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            # now everything to the left of pivot is <= pivot
            # and everything to the right is > pivot
            if p == target:
                return nums[p]
            if p < target:
                return quickSort(p + 1, r)
            else:
                return quickSort(l, p - 1)
        return quickSort(0, len(nums) - 1)



            
                


                

        
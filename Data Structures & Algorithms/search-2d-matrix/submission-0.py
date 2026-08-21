class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # This looks like two binary searches
        # First we search along the columns
        # is it between middle row values (within 10 and 13)?
        # if smaller we shift mid down
        # if larger we shift mid up
        # Then we search within the correct row with normal bs

        l, r = 0, len(matrix) - 1
        row_index = -1
        while l <= r:
            mid = (l + r) // 2
            low, high = matrix[mid][0], matrix[mid][-1]
            if target <= high and target >= low:
                # set correct row and exit loop
                row_index = mid
                break
            elif target < low:
                r = mid - 1
            elif target > high:
                l = mid + 1
        if row_index == -1:
            return False
        
        row = matrix[row_index]
        l, r = 0, len(row) - 1
        while l <= r:
            mid = (l + r) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
        


        
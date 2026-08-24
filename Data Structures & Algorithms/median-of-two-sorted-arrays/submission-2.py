class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B)<len(A):
            A, B = B, A
        l1, r1 = 0, len(A) - 1
        total = len(nums1) + len(nums2)
        half = total // 2

        while True:
            mid1 = (l1 + r1) // 2
            mid2 = half - mid1 - 2

            Aleft = A[mid1] if mid1 >= 0 else float("-infinity")
            Aright = A[mid1 + 1] if mid1 + 1 < len(A) else float("infinity")
            Bleft = B[mid2] if mid2 >= 0 else float("-infinity")
            Bright = B[mid2 + 1] if mid2 + 1 < len(B) else float("infinity")
            # check if our partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                operand1 = max(Aleft,Bleft)
                operand2 = min(Aright,Bright)
                if total % 2 == 0:
                    return (operand1 + operand2) / 2
                else:
                    return operand2
            elif Aleft > Bright:
                r1 = mid1 - 1
            else:
                l1 = mid1 + 1


        
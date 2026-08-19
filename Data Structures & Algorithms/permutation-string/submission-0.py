class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # idea, take a window of size of s1
        # create a count list of size 26 for the window
        # check it against the og count.
        # if it's the same, return true, else shift forward
        if len(s1) > len(s2):
            return False
    
        count = [0] * 26
        for c in s1:
            count[ord(c) - ord("a")] += 1
        # intialize window and first count
        l, r = 0, len(s1) - 1
        window_count = [0] * 26
        for i in range(len(s1)):
            window_count[ord(s2[i]) - ord("a")] += 1
        while r < len(s2):
            if count == window_count:
                return True
            else:
                window_count[ord(s2[l]) - ord("a")] -= 1
                l += 1
                r += 1
                if r == len(s2):
                    return False
                window_count[ord(s2[r]) - ord("a")] += 1
        return False



        
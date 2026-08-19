class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # new solution:
        # start with full window
        # get the best length we can do by shrinking the window leftward
        # now take this window and shift it to the right
        # at each point we check: 
        # - is the window valid? If not, shift againt
        # - if it is: can we remove the far right index?
        # - if yes, repeat. Then start shifting this new size window
        # if right goes out of range, just shift left
        # if right is at the far end and the window is not valid, end the
        # loop
        smallest_s = ""
        freq = defaultdict(int)
        need = 0
        for c in t:
            freq[c] += 1
            need += 1 
        
        window = defaultdict(int)
        l, r = 0, len(s) - 1
        for c in s:
            window[c] += 1
        
        # check if a valid window even exists
        for key in freq.keys():
            if window[key] < freq[key]:
                return ""

        # shrink window back until it is valid
        valid = True
        while valid:
            if window[s[r]] - 1 >= freq[s[r]]:
                window[s[r]] -= 1
                r -= 1
            else:
                valid = False
        smallest_window = s[l:r+1]

        if l == r:
            return smallest_window

        have = need
        while True:
            # pop of the left side to see if we can make a smaller window
            window[s[l]] -= 1
            if window[s[l]] < freq[s[l]]:
                have -= 1
            l += 1
            # extend window rightward until valid
            while have != need and r != len(s) - 1:
                r += 1
                window[s[r]] += 1
                if window[s[r]] ==  freq[s[r]]:
                    have += 1
            # if window hit the end and the window isn't valid, return
            if r == len(s) - 1 and have != need:
                return smallest_window
            # if we reach a valid window, pop off left amap
            while True:
                if window[s[l]] == freq[s[l]]:
                    break
                else:
                    window[s[l]] -= 1
                    l += 1
            if len(smallest_window) > len((s[l:r+1])):
                smallest_window = s[l:r+1]
        return smallest_window
                




    

        
        



        
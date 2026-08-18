class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        #initialize first window
        l, r = 0, 0
        count[ord(s[0]) - ord("A")] = 1
        max_len = 0;
        window_chars = set()
        window_chars.add(s[0])

        while r < len(s):
            # find the highest freq in window
            h_freq = 0
            for elm in window_chars:
                h_freq = max(h_freq, count[ord(elm) - ord("A")])
            # expand window
            window_size = r + 1 - l
            if window_size - h_freq <= k:
                max_len = max(max_len, window_size)
                r += 1
                if r == len(s):
                    return max_len
                count[ord(s[r]) - ord("A")] += 1
                window_chars.add(s[r])
            # shrink window
            else:
                l += 1
                count[ord(s[l - 1]) - ord("A")] -= 1
        return max_len


            

        
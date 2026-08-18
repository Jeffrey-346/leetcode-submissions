class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maintain a map of from letter to index.
        # check if new letter is in map. If not, add it and ++1 len
        # if it is, then get the index of the previous occurence of the
        # letter -> the substring starts the character after that
        # calculate distance and then keep scanning forward...

        old_pos = {}
        max_len = 0
        curr_len = 0
        for i in range(len(s)):
            if s[i] not in old_pos.keys() or i - old_pos[s[i]] > curr_len:
                curr_len += 1
                old_pos[s[i]] = i
                max_len = max(curr_len, max_len)
            else:
                curr_len = i - old_pos[s[i]]
                old_pos[s[i]] = i
        return max_len


        
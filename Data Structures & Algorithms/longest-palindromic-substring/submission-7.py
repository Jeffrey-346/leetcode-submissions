class Solution:
    def longestPalindrome(self, s: str) -> str:
        # take each letter as the middle of the palindrome
        # expand outwards as far as possible
        mLen = 0
        start = None
        end = None
        for i in range(len(s)):
            # odd
            length = 0
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > mLen:
                    mLen = length
                    start = l
                    end = r + 1
                l -= 1
                r += 1
            # even
            length = 0
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > mLen:
                    mLen = length
                    start = l
                    end = r + 1
                l -= 1
                r += 1
        print(mLen)
        return s[start:end]


        
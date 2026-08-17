class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer problem
        # initialize to beginning and end of string
        # skip any non-alphanumeric characters, compare, increment forward
        # /back

        anumeric = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")
        l, r = 0, len(s) - 1
        while l < r:
            while s[l] not in anumeric:
                l += 1
                if l == r:
                    return True
            while s[r] not in anumeric:
                r -= 1
                if l == r:
                    return True
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True

        
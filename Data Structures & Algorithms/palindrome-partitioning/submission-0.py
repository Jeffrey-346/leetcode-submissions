class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # split or don't split
        # do it for each letter
        # but if the current str is not yet a palindrome, no
        # need to split here (invalid)
        # maintiain current list
        # if there are no more letters, check if curr is a palindrome
        # if it is, append list to res

        # how are we checking if the current str is a palindrome?
        # start naively by going through each letter
        res = []
        lst = []
        def dfs(start, end):
            if start == end:
                res.append(lst.copy())
            # split
            for i in range(start, end):
                if isPalindrome(s[start:i + 1]):
                    lst.append(s[start:i + 1])
                    dfs(i + 1, end)
                    lst.pop()

        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        dfs(0, len(s))
        return res

        
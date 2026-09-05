class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # map digit char to string
        # use backtracking to go through every combination
        # iteration depth tells which number we are processing
        # stop when iteration depth hits len of digits
        if not digits:
            return []
        digit_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        s = []

        def dfs(i):
            if i == len(digits):
                res.append("".join(s))
                return
            for letter in digit_map[digits[i]]:
                s.append(letter)
                dfs(i + 1)
                s.pop()
        dfs(0)
        return res
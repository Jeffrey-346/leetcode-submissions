class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            for word in wordDict:
                if len(word) > i:
                    continue
                if dp[i - len(word)] and s[i - len(word):i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


        
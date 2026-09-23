class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dfs(i): # number of ways to decode for str starting at i
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            res = dfs(i + 1)
            if i < len(s) - 1 and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res
        
        return dfs(0)



        
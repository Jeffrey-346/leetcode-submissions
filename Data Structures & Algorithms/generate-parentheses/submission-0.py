class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # ok each level of this tree has 4 branches
        # ()_, _(), (_, _(
        # have a "seen" set to reduce duplicates
        def dfs(s, open, close):
            if len(s) == 2 * n:
                res.append(s)
                return

            if open < n:
                dfs(s + "(", open + 1, close)

            if close < open:
                dfs(s + ")", open, close + 1)
        dfs("", 0, 0)
        return res
            
        
            
                
        
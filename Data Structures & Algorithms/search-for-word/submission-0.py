class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # for each letter, backtrack and try to explore every
        # possible direction
        # path is a set of indices, the places we've traveled
        # index: [row, column]
        if not board:
            return False
        def dfs(row, col, path, k):
            if word[k] != board[row][col]:
                return False
            if k == len(word) - 1:
                return True
            path.add((row, col))
            res1 = res2 = res3 = res4 = False
            # append current index to our "string" list
            # try to go right
            if col < len(board[0]) - 1 and (row, col + 1) not in path:
                res1 = dfs(row, col + 1, path, k + 1)
            # try to go left
            if col > 0 and (row, col - 1) not in path:
                res2 = dfs(row, col - 1, path, k + 1)
            # try to go down
            if row < len(board) - 1 and (row + 1, col) not in path:
                res3 = dfs(row + 1, col, path, k + 1)
            # try to go up
            if row > 0 and (row - 1, col) not in path:
                res4 = dfs(row - 1, col, path, k + 1)
            # backtrack
            path.remove((row, col))
            return res1 or res2 or res3 or res4

        for i in range(len(board)):
            for j in range(len(board[0])):
                res = dfs(i, j, set(), 0)
                if res:
                    return True
        return False
            
            
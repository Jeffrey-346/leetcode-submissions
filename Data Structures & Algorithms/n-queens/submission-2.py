class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # initialize board all '.'
        board = [['.' for _ in range(n)] for _ in range(n)]

        # - check for current row, each valid index in the current row
        # - place a queen at each valid index
        # - helper to mark invalid cells across board for a given queen 
        #   placement
        # - explore next depth (next row)
        # - if there are no valid indices, stop this exploration

        def dfs(i):
            if i == n:
                elm = []
                for j in range(n):
                    elm.append("".join(board[j]))
                res.append(elm)
                return
            curr_row = board[i]
            for j in range(n):
                if isValid(i, j):
                    curr_row[j] = 'Q'
                    dfs(i + 1)
                    curr_row[j] = '.'
        
        def isValid(row, col):
            if row == 0:
                return True
            count = 1
            for i in range(row - 1, -1, -1):
                # check directly above
                if board[i][col] == 'Q':
                    return False
                # check diagonal left
                if col - count >= 0:
                    if board[i][col - count] == 'Q':
                        return False
                if col + count < n:
                    if board[i][col + count] == 'Q':
                        return False
                count += 1
            return True
        dfs(0)
        return res

        

            

        
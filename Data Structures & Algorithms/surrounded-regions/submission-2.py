class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # so any 0 region connected to the edge of the board somehow is safe. 
        # Let's use a similar strategy to last question...
        # get a set of all the 0 coordinates on the outer edge of the board
        # perform dfs for each cell to add them to the set of safe 0's
        # Finally go through the board and if any cell is 0 and not in safe then
        # switch it to X

        safe = set()
        for row in range(len(board)):
            if board[row][0] == 'O':
                safe.add((row, 0))
            if board[row][len(board[0]) - 1] == 'O':
                safe.add((row, len(board[0]) - 1))

        for col in range(len(board[0])):
            if board[0][col] == 'O':
                safe.add((0, col))
            if board[len(board) - 1][col] == 'O':
                safe.add((len(board) - 1, col))
        
        stack = list(safe)
        while stack:
            new_stack = []
            for row, col in stack:
                if row > 0 and (row - 1, col) not in safe and board[row - 1][col] == 'O':
                    safe.add((row - 1, col))
                    new_stack.append((row - 1, col))
                if row < len(board) - 1 and (row + 1, col) not in safe and board[row + 1][col] == 'O':
                    safe.add((row + 1, col))
                    new_stack.append((row + 1, col))
                if col > 0 and (row, col - 1) not in safe and board[row][col - 1] == 'O':
                    safe.add((row, col - 1))
                    new_stack.append((row, col - 1))
                if col < len(board[0]) - 1 and (row, col + 1) not in safe and board[row][col + 1] == 'O':
                    safe.add((row, col + 1))
                    new_stack.append((row, col + 1))
            stack = new_stack
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O' and (row, col) not in safe:
                    board[row][col] = 'X'




        
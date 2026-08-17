class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use a hashmap and map box number to a tuple of length 9
        # initialized to 0. Then if the number is in the box we
        # intialize that index to 1. If the number appears again then
        # we can return false. 

        # rows we can just go row-wise with a for loop
        # for columns we can have a columns dictionary

        # starting with rows
        for row in board:
            filled = [0] * 9
            for cell in row:
                if cell != ".":
                    num = int(cell) - 1
                    if filled[num] != 0:
                        return False
                    filled[num] = 1

        # now cols
        filled_cols = [[0] * 9 for i in range(len(board))]
        for row in board:
            for i in range(len(row)):
                if row[i] != ".":
                    num = int(row[i]) - 1
                    if filled_cols[i][num] != 0:
                        return False
                    filled_cols[i][num] = 1
        
        # now boxes
        filled_boxes = [[0] * 9 for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    num = int(board[i][j]) - 1
                    # multiply hor by 3 + ver
                    hor = i // 3
                    ver = j // 3
                    if filled_boxes[hor * 3 + ver][num] != 0:
                        return False
                    filled_boxes[hor * 3 + ver][num] = 1
        
        return True
                



        
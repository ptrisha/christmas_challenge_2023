# Leetcode problem for Dec 20
# Problem description:
# https://leetcode.com/problems/valid-sudoku

# Thankfully, a relatively easy, straightforward problem compared with
# those of the past few days.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def _isValidSet(cells: List[str])-> bool:
            
            digitFlags = [False]*9

            for s_int in cells:
                if s_int != ".":
                    digit = int(s_int)
                    if digitFlags[digit-1]:
                        return False
                    else:
                        digitFlags[digit-1]=True
                
            return True


        # check rows
        num_rows = len(board)
        for row in board:
            if not _isValidSet(row):
               return False

        # check columns
        num_cols = len(board)
        for n in range(num_cols):
            col = []
            # iterate across rows for a fixed column
            for m in range(num_rows):
                col.append(board[m][n])
                
            if not _isValidSet(col):
                return False

        # check squares
        subboxCoords = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2),(2,0), (2,1), (2,2)]
        num_blocks_in_dim = 3

        for row_block in range(num_blocks_in_dim):

            for col_block in range(num_blocks_in_dim):
                coords = [ (r+row_block*3, c+col_block*3) for (r, c) in subboxCoords ]

                # get contents of cells of coords
                cells = [ board[r][c] for (r,c) in coords ]

                if not _isValidSet(cells):
                    return False

        return True
    
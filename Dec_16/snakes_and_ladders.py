# Leetcode problem for Day 16
# Problem description:
# https://leetcode.com/problems/snakes-and-ladders

# BFS algorithm using queue as data structure
# Had the help of video at:
# https://www.youtube.com/watch?v=6lH4nO3JfLk ,
# and BFS algo at:
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        length = len(board)     # board dim are length X length

        board.reverse()    # reverse so the bottom row is the first element of list
         
        destination = length*length - 1

        # an internal function to convert cell number to [row, col]
        # Note: here, we assume the cellNum to be zero-based
        def labelToRC(cellNum: int, ) -> (int, int):
            # compute the row
            row = cellNum // length
            col = cellNum % length
            # compute the column dim based on alternating row directions
            if row%2==1:
               col = length - 1 - col
            return (row, col)

        # BFS algorithm using queue

        # marker for visited cells, initialised to False
        visited = [False]*(length*length)

        # create a queue 
        queue = []

        # start with the first cell, mark it visited and enqueue it
        queue.append([0,0])  # cell info: [cell_label-1, no. of moves]

        while queue:
            # deque the first element
            [cellNum, moves] = queue.pop(0)

            for i in range(1, 7):

                nextCell = cellNum + i
                # get the row, col dim of the cell
                (row, col) = labelToRC(nextCell)
            
                cellDir = board[row][col]
                if cellDir != -1:
                    nextCell = cellDir-1
                if nextCell == destination:
                    return moves+1
            
                if not visited[nextCell]:
                   queue.append([nextCell, moves+1])
                   visited[nextCell] = True

        
        # Destination is not reached at this point
        return -1
    
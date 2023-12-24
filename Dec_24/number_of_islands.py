# Leetcode problem for Dec 24
# Problem description:
# https://leetcode.com/problems/number-of-islands

# This version (using BFS) is done with help from video:
# https://www.youtube.com/watch?v=pV2kpPD66nE

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # record the cells that have been visited
        visited = set()
        # find dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(row: int, col: int) -> None:
            que = collections.deque()
            directions = [ [-1, 0], [1, 0], [0, 1], [0, -1]]
            visited.add( (row, col) )
            que.append( (row, col) )

            while que:
                curr_row, curr_col = que.popleft()
                for dr, dc in directions:
                    r = curr_row + dr
                    c = curr_col + dc
                    if r in range(rows) and c in range(cols) and \
                       grid[r][c] == "1" and (r,c) not in visited:
                       visited.add((r, c))
                       que.append((r, c))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and ((row, col) not in visited):
                    bfs(row, col)
                    islands += 1

        return islands
                    



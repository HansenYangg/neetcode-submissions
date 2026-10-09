class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        res = 0 
        visited = set()

        def dfs(r, c):
            stack = [(r, c)]

            while stack:
                row, col = stack.pop()
            
                if row > 0 and grid[row - 1][col] == "1" and (row - 1, col) not in visited:
                    stack.append((row - 1, col))
                    visited.add((row - 1, col))
                if col > 0 and grid[row][col - 1] == "1" and (row, col - 1) not in visited:
                    stack.append((row, col - 1))
                    visited.add((row, col - 1))
                if row < len(grid) - 1 and grid[row + 1][col] == "1" and (row + 1, col) not in visited:
                    stack.append((row + 1, col))
                    visited.add((row + 1, col))
                if col < len(grid[0]) - 1 and grid[row][col + 1] == "1" and (row, col + 1) not in visited:
                    stack.append((row, col + 1))
                    visited.add((row, col + 1))




        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    res += 1

        return res

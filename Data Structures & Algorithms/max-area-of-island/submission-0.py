class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()

        def dfs(r, c, visited):
            stack = [(r, c)]
            res = 0
            while stack:
                row, col = stack.pop()
                if grid[row][col] == 1 and (row, col) not in visited:
                    visited.add((row, col))
                    res += 1
                    if row < len(grid) - 1:
                        stack.append((row + 1, col))
                    if row > 0:
                        stack.append((row - 1, col))
                    if col > 0:
                        stack.append((row, col - 1))
                    if col < len(grid[0]) - 1:
                        stack.append((row, col + 1))


            return res



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c, visited))


        return res
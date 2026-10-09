class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        res = 0 
        visited = set()

        def dfs(r, c):
            stack = [(r, c)]

            while stack:
                row, col = stack.pop()
                dirs = [(0, -1), (-1, 0), (1, 0), (0, 1)]
                for direction in dirs:
                    nr, nc = row + direction[0], col + direction[1]
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        stack.append((nr, nc))
                        visited.add((nr, nc))




        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    res += 1

        return res

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        res = 0 
        visited = set()

        def dfs(r, c, visited):
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                if grid[r][c] == "1":
                    if (r, c) not in visited:
                        visited.add((r, c))

                        if r < len(grid) - 1:
                            stack.append((r + 1, c))
                        if r > 0:
                            stack.append((r - 1, c))
                        if c < len(grid[0]) - 1:
                            stack.append((r, c + 1))
                        if c > 0:
                            stack.append((r, c - 1))
                






        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                    dfs(r, c, visited)

        return res
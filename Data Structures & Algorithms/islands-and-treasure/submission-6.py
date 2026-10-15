class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        inf = 2**31 - 1

        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
       
        visited = set()
        d = 0
        while q:
            d += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

                for row, col in dirs:
                    nr, nc = r + row, c + col
                    
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited:
                        if grid[nr][nc] == inf:
                            grid[nr][nc] = d
                            

                            visited.add((nr, nc))
                            q.append((nr, nc))


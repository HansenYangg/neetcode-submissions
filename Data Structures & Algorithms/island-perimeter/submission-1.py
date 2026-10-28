class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        res = 0
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        # of edges for a given land square is 4 - # of touching islands to it

        visited = set()
        def dfs(row, col):
            nonlocal res

            stack = [(row, col)]
            visited.add((row, col))
            
            while stack: 
              
                r, c = stack.pop()
                walls = 4

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        
                        if (nr, nc) not in visited:
                    
                            stack.append((nr, nc))
                            visited.add((nr, nc))

                        walls -= 1
              
                   
                
                res += walls



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return res

        return res
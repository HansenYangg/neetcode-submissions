class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''

        iterate through every row and column in grid[r][c], and if it is a rotten fruit, subtract n from 1
        perform a bfs on it; if any neighbors are a fresh fruit, we update them to become 
        rotten, and add them to the queue. also maintain a visited set so we don't unnecessarily perform actions

        after all bfs is done, iterate through the grid, if any are equal to 1, then we return -1, else return the number of turns we took before bfs terminated
        
        '''
        res = fresh = 0
        queue = deque()
        visited = set()
    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
                    
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r, c) not in visited:
                    visited.add((r, c))
                    # check 4 dirs
                    # within the 4 dirs, need to update fresh fruit to rotten fruit, and add to queue only if they were fresh 
                    if r < len(grid) - 1:
                        if grid[r + 1][c] == 1:
                            grid[r + 1][c] = 2
                            queue.append((r + 1, c))
                            fresh -= 1
                    if r > 0:
                        if grid[r - 1][c] == 1:
                            grid[r - 1][c] = 2
                            queue.append((r - 1, c))
                            fresh -= 1

                    if c < len(grid[0]) - 1:
                        if grid[r][c + 1] == 1:
                            grid[r][c + 1] = 2
                            queue.append((r, c + 1))
                            fresh -= 1

                    if c > 0:
                        if grid[r][c - 1] == 1:
                            grid[r][c - 1] = 2
                            queue.append((r, c - 1))
                            fresh -= 1
            if queue:
                res += 1


        return res if fresh == 0 else -1

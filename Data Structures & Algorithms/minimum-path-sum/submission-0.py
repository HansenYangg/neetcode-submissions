class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0


        dp = []
        r, c = len(grid), len(grid[0])
        for _ in range(r):
            dp.append([0] * c)

        dp[0][0] = grid[0][0]

        for row in range(r):
            for col in range(c):
                if row == 0 and col == 0:
                    continue
                elif row == 0:
                    dp[row][col] = grid[row][col] + dp[row][col - 1]
                
                elif col == 0:
                    dp[row][col] = grid[row][col] + dp[row - 1][col]

                else:
                    dp[row][col] = grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])
                
        return dp[r - 1][c - 1]
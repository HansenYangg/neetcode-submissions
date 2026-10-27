class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        dp = [ [0] * n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                elif r == 0:
                    dp[r][c] = grid[r][c] + dp[r][c - 1]

                elif c == 0:
                    dp[r][c] = grid[r][c] + dp[r - 1][c]

                else:
                    dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])
        print(dp)
        return dp[m - 1][n - 1]
'''
[1, 3, 3], 
[5, 7, 5], 
[1, 2, 5]]


'''

        
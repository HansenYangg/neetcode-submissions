class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(row, col):
            if row == m - 1 and col == n - 1:
                return 1

            if (row, col) in memo:
                return memo[(row, col)]

            if col == n - 1:
                ans = dp(row + 1, col)
            elif row == m - 1:
                ans = dp(row, col + 1)
            else:
                ans = dp(row + 1, col)
                ans += dp(row, col + 1)
            

            memo[(row, col)] = ans
            return memo[(row, col)]


            

        return dp(0, 0)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)

        def dp(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            if memo[i] == -1:
                val = cost[i] + min(dp(i + 1), dp(i + 2))
                memo[i] = val
                return val
            else:
                return memo[i]

        return min(dp(0), dp(1))



class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(curr, i):
            if curr == target and i == len(nums):
                return 1
            
            if (curr, i) in memo:
                return memo[(curr, i)]

            if i >= len(nums):
                return 0

            ans = dp(curr + nums[i], i + 1)
            ans += dp(curr - nums[i], i + 1)

            memo[(curr, i)] = ans

            return memo[(curr, i)]


        return dp(0, 0)
            


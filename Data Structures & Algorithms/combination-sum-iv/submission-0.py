class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
        memo where we store how much ways we can reach target from our current sum
        dp approach 

        '''

        memo = {}


        def dp(currSum):

            if currSum == target:
                return 1

            if currSum in memo:
                return memo[currSum]
            
            if currSum > target:
                return 0

            # take current num and stay at same indx (reuse), and move onto next indx and do not reuse
            ans = 0
            for i in range(len(nums)):
                ans += dp(currSum + nums[i])


            memo[currSum] = ans
            return memo[currSum]


        return dp(0)

            
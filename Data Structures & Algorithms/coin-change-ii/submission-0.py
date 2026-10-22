class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dp(currAmount, idx):
            if currAmount == amount:
                return 1

            if idx >= len(coins) or currAmount > amount:
                return 0

            if (currAmount, idx) in memo:
                return memo[(currAmount, idx)]


            
            ans = dp(currAmount + coins[idx], idx)
            ans += dp(currAmount, idx + 1)

            memo[(currAmount, idx)] = ans
            return memo[(currAmount, idx)]

        return dp(0, 0)
        
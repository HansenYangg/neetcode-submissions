class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        if sum(matchsticks) % 4 != 0:
            return False

        res, used, target = False, [False] * len(matchsticks), sum(matchsticks) // 4

        def backtrack(curr, sides, i):

            nonlocal res

            if res:
                return 

            if sides == 0:
                res = True
                return
              
            if curr == target:
                backtrack(0, sides - 1, 0)
                return
            
            if i >= len(matchsticks):
                return

            for idx, val in enumerate(matchsticks[i:], start=i):
                if used[idx] == False and curr + matchsticks[idx] <= target:
                    used[idx] = True
                    backtrack(curr + matchsticks[idx], sides, idx + 1)
                    used[idx] = False


        backtrack(0, 4, 0)
        return res
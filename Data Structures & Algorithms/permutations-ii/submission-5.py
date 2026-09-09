class Solution:
    from collections import Counter
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(curr, i):
            if len(curr) == len(nums):
                res.add(tuple(curr))
                    
                return

            if i >= len(nums):
                return 

            for idx, val in enumerate(nums):
                if val != float("inf"):
                    nums[idx] = float("inf")
                    backtrack(curr + [val], idx)
                    nums[idx] = val

                            
          
        backtrack([], 0)
        return list(res)
class Solution:
    from collections import Counter
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(curr):
            if len(curr) == len(nums):
                res.add(tuple(curr))
                    
                return

          
            for idx in range(len(nums)):
                if nums[idx] != float("inf"):
                    temp = nums[idx]
                    nums[idx] = float("inf")
                    backtrack(curr + [temp])
                    nums[idx] = temp

                            
          
        backtrack([])
        return list(res)
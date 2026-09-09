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

            for idx in range(len(nums)):
                if nums[idx] != float("inf"):
                    temp = nums[idx]
                    nums[idx] = float("inf")
                    backtrack(curr + [temp], idx)
                    nums[idx] = temp

                            
          
        backtrack([], 0)
        return list(res)
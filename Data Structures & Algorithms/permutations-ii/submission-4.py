class Solution:
    from collections import Counter
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = set()

        def backtrack(curr, string, i):
            if len(curr) == len(nums):
                if string not in s:
                    res.append(curr.copy())
                    s.add(string)
                    return 
                return

            if i >= len(nums):
                return 

            for idx, val in enumerate(nums):
                if val != float("inf"):
                    nums[idx] = float("inf")
                    backtrack(curr + [val], string + str(val), idx)
                    nums[idx] = val

                            
          
        backtrack([], "", 0)
        return res
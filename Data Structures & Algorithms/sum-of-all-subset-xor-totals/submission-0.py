class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def backtrack(curr, i):
            nonlocal res
            res += curr
            if i >= len(nums):
                return
      
            for idx, val in enumerate(nums[i:], start=i):
                backtrack(curr ^ val, idx + 1)

        backtrack(0, 0)
        return res

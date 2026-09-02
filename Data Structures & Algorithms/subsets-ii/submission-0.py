class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(nums, curr, i):
            res.append(curr.copy())
            if len(curr) == len(nums):
                return
            
            for idx, num in enumerate(nums[i:], start=i):
                if idx > i and nums[idx] == nums[idx - 1]:
                    continue
                backtrack(nums, curr + [num], idx + 1)


        backtrack(nums, [], 0)
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return 
                
            for i in range(len(nums)):
                if nums[i] not in arr:
                    backtrack(nums, arr + [nums[i]])

        backtrack(nums, [])
        return res
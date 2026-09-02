class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, curr, indx):
            nonlocal res
            res.append(curr.copy())
            if len(curr) == len(nums):
                return

            for indx, num in enumerate(nums[indx:], start=indx):
                curr.append(num)
                backtrack(nums, curr, indx + 1)
                curr.pop()

            
            


        backtrack(nums, [], 0)
        return res
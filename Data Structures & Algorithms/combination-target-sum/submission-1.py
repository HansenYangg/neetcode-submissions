class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(nums, curr_arr, curr_val, i):
            nonlocal res
            if curr_val == target:
                res.append(curr_arr.copy())
                return 
            if curr_val > target:
                return 

            for indx, num in enumerate(nums[i:], start=i):
                curr_arr.append(num)
                curr_val += num
                backtrack(nums, curr_arr, curr_val, indx)

                curr_arr.pop()
                curr_val -= num
            

        backtrack(nums, [], 0, 0)
        return res

            
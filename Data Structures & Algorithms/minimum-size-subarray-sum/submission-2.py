class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res, curr_sum, curr_len, l = float("inf"), 0, 0, 0
        for r in range(len(nums)):
            curr_sum, curr_len = curr_sum + nums[r], curr_len + 1

            while curr_sum >= target:
                res, curr_sum, curr_len, l = min(res, curr_len), curr_sum - nums[l], curr_len - 1, l + 1


        return 0 if res == float("inf") else res





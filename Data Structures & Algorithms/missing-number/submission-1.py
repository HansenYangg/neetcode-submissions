class Solution:
    def missingNumber(self, nums: List[int]) -> int:
            n = len(nums) + 1


            expected_sum = (n*(n-1))/2
            actual = sum(nums)
            return int(expected_sum - actual)


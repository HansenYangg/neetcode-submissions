class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = currMin = 1
        res = nums[0]
        for num in nums:
            temp = currMax
            currMax = max(currMin * num, num, temp * num)

            currMin = min(temp * num, currMin * num, num)
            res = max(res, currMax)

        return res

        
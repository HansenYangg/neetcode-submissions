class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
            
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if m == 0 and nums[m] > nums[m + 1]:
                return 0

            if m == len(nums) - 1 and nums[m] > nums[m - 1]:
                return m

            if m - 1 >= 0 and m + 1 < len(nums) and nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m

            if m + 1 < len(nums):
                if nums[m] < nums[m + 1]:
                    l = m + 1
                else:
                    r = m - 1


            '''
            [1,2,1,3,4]

            '''
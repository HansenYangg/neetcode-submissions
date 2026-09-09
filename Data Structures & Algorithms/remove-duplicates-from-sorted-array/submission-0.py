class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        res = 1
        for i in range(len(nums)):
            if nums[i] != nums[write - 1]:
                nums[write] = nums[i]
                write += 1
                res += 1

        return res
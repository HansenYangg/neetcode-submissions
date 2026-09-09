class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        vals = [i for i in range(len(nums)) if nums[i] == val]

        while vals:
            nums[vals.pop()] = nums[-1]
            nums.pop()

        return len(nums)
# [0,1,2,2,3,0,4] 
# [2, 3]
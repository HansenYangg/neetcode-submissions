class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        goal = len(nums) - 1
        # start from 2nd to last element and iterate backwards
        # if we can reach our current goal with the amount of steps we have at our curr pos
        # update goal to that new pos
        # continue iterating backwards and continuously and see if we can reach our curr goal with the amount of jumps we have at our pos
        # return true if goal is 0 
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
            




        return goal == 0
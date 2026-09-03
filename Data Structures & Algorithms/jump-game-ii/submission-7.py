class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = i = 0
        while i < len(nums) - 1:
            curr_highest = 0
            jumpTo = None

            for j in range(i + 1, i + 1 + nums[i]):
                if j >= len(nums) - 1:
                    return steps + 1
                if nums[j] + j >= curr_highest:
                    curr_highest = nums[j] + j
                    jumpTo = j
                    

            i = jumpTo
            steps += 1
                    



        return steps
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        m = {} # {3:0}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in m:
                return [m[needed], i]
            else:
                m[nums[i]] = i 



            
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in mapping:
                return [mapping[need], i]
            mapping[nums[i]] = i
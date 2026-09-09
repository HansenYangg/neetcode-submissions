class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        s = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                curr, l, r = nums[i] + nums[j], j + 1, len(nums) - 1
                while l < r:

                   

                    if curr + nums[l] + nums[r] == target:
                        if (nums[i], nums[j], nums[l], nums[r]) not in s:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                            s.add((nums[i], nums[j], nums[l], nums[r]))
                        
                        
                        l, r = l + 1, r - 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

                    elif curr + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1





        return res

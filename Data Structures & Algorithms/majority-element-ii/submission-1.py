class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = [] #O(k) space
        m = {} 
        n = int(len(nums) / 3) 

        for num in nums:
            if num in m:
                m[num] += 1
                
            else:
                m[num] = 1
            if m[num] > n + 1:
                continue

            elif m[num] > n:
                res.append(num)

        return res
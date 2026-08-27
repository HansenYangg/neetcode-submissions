class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr = 0
        highest = 0
        s = set(nums) #O(N)

        for num in nums: #O(N)
            if num - 1 not in s:
                curr, temp = 1, num
                while temp + 1 in s:
                    curr, temp = curr + 1, temp + 1
                highest = max(highest, curr) 

        return highest 

            
            
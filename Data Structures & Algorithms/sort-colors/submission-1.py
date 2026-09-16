class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        3 variables, ones, twos, threes
        one pass to tally up how much of each of these variables are 
        """
      
        zeros = ones = twos = 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
               twos += 1

        idx = 0
        print(len(nums))
        
        while zeros > 0:
            print(idx)
            nums[idx] = 0
            idx += 1
            zeros -= 1

        while ones > 0:
            nums[idx] = 1
            idx += 1
            ones -= 1

        while twos > 0:
            nums[idx] = 2
            idx += 1
            twos -= 1

            

        
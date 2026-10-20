class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        '''
        sliding window approach -> iterate through nums:
        if we encounter a 1: increase our current window size by 1
        else (encounter 0):
            decrement how much flips we have left
                if flips still >= 0, increase window size by 1
                otherwise, need to shrink window from the left until we encounter a 0, so we regain a flip we can use on the current 0. shrink window size by 1
        edge cases:
        if k is 0, just need to find longest sequence of k 
        '''
        max_window = curr_window = l = 0
        for r in range(len(nums)):
            if nums[r] == 1: 
                curr_window += 1

            else:
                k -= 1
                if k >= 0: # have k's to spare or at the limit ; can just still increment curr window
                    curr_window += 1
                else:
                    while nums[l] == 1: # need to find a zero to remove from the left 
                        
                        l += 1
                        curr_window -= 1
                 
                    l += 1
                    k += 1
                    

                    




            max_window = max(max_window, curr_window)




        return max_window
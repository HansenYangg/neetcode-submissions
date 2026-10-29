class Solution:
    from collections import defaultdict

    def subarraySum(self, nums: List[int], k: int) -> int:
        '''

        prefixes map 
        for any current prefix sum, the complement we need is k - curr prefix sum. we check how much of that is in our map, and add that to some sort of answer

        '''
        prefixes = { 0 : 1 }
    

        ans = 0

        # build prefixes map

        curr = 0
        for num in nums:
            curr += num

            needed = curr - k
            if needed in prefixes:

                ans += prefixes[needed]
                
            if curr in prefixes:
                prefixes[curr] += 1
            else:
                prefixes[curr] = 1
                

        
        

        return ans

            
            



            

        

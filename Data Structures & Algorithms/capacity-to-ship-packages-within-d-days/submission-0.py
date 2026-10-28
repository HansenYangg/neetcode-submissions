class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        binary search from max(weights) to sum(weights)

        for each midpoint, simulate seeing how much days it'll take for all packages to ship
        if days <= how much days we have, we can try lower weight values (discard all elements to the right; r = m - 1) 

        if days > how much days we have, we know any weight capabity lower than our midpoint will also not work, so we can discard all left weight capacities (l = m + 1) ; need to try bigger values 


        '''

        l, r = max(weights), sum(weights)

        ans = r

        while l <= r:

            m = (l + r) // 2
            
            daysTaken = idx = 0

            temp = m
         

            while idx < len(weights):
                while idx < len(weights) and m >= weights[idx]:
                    m -= weights[idx]
                    idx += 1

                m = temp
                daysTaken += 1
                
            
         
        
            if daysTaken <= days:
                ans = temp
                r = m - 1

            else:
                l = m + 1


        return ans
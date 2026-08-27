class Solution:

    import math

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search, l and r = 1, max(piles)
        # with each k (middle element of l and r), we iterate through the
        # array and do ceil(piles[i] / k)

        #if k works, then we still continue going lower and continue binary serch because there could still be a lower working value
        l, r, res = 1, max(piles), float('inf')

        while l <= r:
            k = l + (r - l) // 2

            needed_h = 0
            for pile in piles:
                needed_h += math.ceil(pile / k)
            
            if needed_h <= h:
                r = k - 1
                if int(k) < res:
                    res = int(k)

            else:
                l = k + 1
            

        return res





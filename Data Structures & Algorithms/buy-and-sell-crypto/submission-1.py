class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize max profit (res) to 0
        # curr min to whatever smallest val is as we pass through input arr
            # initialized to be 0th element
        # at every element starting from index 1, we see if element - curr min > res, and update res if it is
        # return res
        if not prices:
            return 0

        res = 0
        curr_min = prices[0]
        for price in prices[1:]:
            if price < curr_min:
                curr_min = price
            res = max(res, price - curr_min)

        return res
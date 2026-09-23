class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        binary search
        l and r (left and right) at values 0 and x respectively
        compute middle value, and see if that value squared is <, >, or equal to x, and adjust our 
        pointers accordingly:

        middle value * middle_value == x, then return middle_value
        if < x, then l = m + 1
        else r = m - 1


        '''
        l, r = 1, x

        while l <= r:
            m = int(l + (r - l) / 2)
            if m * m == x:
                return m

            if m * m < x:
                l = m + 1

            else:

                r = m - 1

        return r
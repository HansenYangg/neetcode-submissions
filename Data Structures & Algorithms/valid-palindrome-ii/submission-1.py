class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
       

        def helper(l, r, deletes):
            if deletes < 0:
                return False

            if l >= r:
                return True

            if s[l] == s[r]:
                return helper(l + 1, r - 1, deletes)
            
            return helper(l + 1, r, deletes - 1) or helper(l, r - 1, deletes - 1)
            


        return helper(0, len(s) - 1, 1)
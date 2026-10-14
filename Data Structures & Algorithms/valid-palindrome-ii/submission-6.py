class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
       
        def helper(l, r, deletion):
            if l >= r:
                return True


            if s[l] == s[r]:
                return helper(l + 1, r - 1, deletion)

            if deletion:
                return helper(l + 1, r, False) or helper(l, r - 1, False)
            return False



        return helper(0, len(s) - 1, True)
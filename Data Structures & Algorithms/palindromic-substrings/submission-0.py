class Solution:
    def countSubstrings(self, s: str) -> int:
        

        res = 0

        for i in range(len(s)):
            res, l, r = res + 1, i - 1, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res, l, r = res + 1, l - 1, r + 1

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                res, l, r = res + 1, i - 1, i + 2

                while l >= 0 and r < len(s) and s[l] == s[r]:
                    res, l, r = res + 1, l - 1, r + 1

        return res

            
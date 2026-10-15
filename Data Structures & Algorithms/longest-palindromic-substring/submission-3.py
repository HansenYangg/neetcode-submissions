class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        res, longest = "", 0


        for i in range(len(s)):
            curr = s[i]

            l, r = i - 1, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    curr, l, r = s[l] + curr + s[r], l - 1, r + 1
                else:
                    break
                    
            if len(curr) > longest:
                longest = len(curr)
                res = curr

        for i in range(len(s) - 1):
            curr = s[i] + s[i + 1]
            if curr == curr[::-1]:
                l, r = i - 1, i + 2
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        curr, l, r = s[l] + curr + s[r], l - 1, r + 1
                    else:
                        break
                        
                if len(curr) > longest:
                    longest = len(curr)
                    res = curr

        return res


                


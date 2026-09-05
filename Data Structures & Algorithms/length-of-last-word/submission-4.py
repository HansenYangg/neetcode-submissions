class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                res = 0
                while i >= 0 and s[i] != " ":
                    i -= 1
                    res += 1
                return res
        

        
                

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                res, idx = 0, i
                while idx >= 0 and s[idx] != " ":
                    idx -= 1
                    res += 1
                return res
        

        
                

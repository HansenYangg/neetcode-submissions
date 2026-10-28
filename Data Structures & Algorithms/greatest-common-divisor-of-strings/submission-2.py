class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str1) == len(str2):
            if str1 == str2:
                return str1

            return ""

        if len(str1) > len(str2): # make str1 always smaller one
            str1, str2 = str2, str1

        curr = str1

        while curr:
            if curr * (len(str2) // len(curr)) == str2 and curr * (len(str1) // len(curr)) == str1:
                return curr

            curr = curr[:-1]
        
        
        return ""
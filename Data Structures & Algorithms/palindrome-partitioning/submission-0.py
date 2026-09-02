class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # essentially a substrings problem, but only keep substrings that are palindromes
        # at every pos, append to result array if it's a palindrome, continue recursing through rest of chars
        # start at ""
        # add a to substring, and a to an array (keep track of pailindromic substring list)

        # go to next index, 
        res = []
        def backtrack(arr, i):
            if i == len(s):
                if arr: 
                    res.append(arr.copy())
                    return 
                else: 
                    return
       
            for end in range(i + 1, len(s) + 1):
                # need to backtrack WITH all chars up to i, but also with just i
                substring = s[i:end] 
                if substring == substring[::-1]:
                    backtrack(arr + [substring], end)
              

                
    
        backtrack([], 0)

        return res

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        res = []
        m = {2:"abc", 3:"def", 4:"ghi",
            5: "jkl", 6: "mno", 7: "pqrs",
            8: "tuv", 9: "wxyz"}

        def backtrack(digits, curr, i):
            if len(curr) == len(digits):
                res.append(curr)
                return 
            
            if len(curr) > len(digits):
                return

            for idx, num in enumerate(digits[i:], start=i):
                for digit in m[int(num)]:
                    backtrack(digits, curr + digit, idx + 1)
            
        
        backtrack(digits, "", 0)
            
        return res

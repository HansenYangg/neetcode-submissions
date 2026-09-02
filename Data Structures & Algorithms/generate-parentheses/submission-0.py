class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, l, r):
            if l == n and r == n:
                res.append(curr)
                return
            if l > n or r > n:
                return
        
            backtrack(curr + "(", l + 1, r)
            if r < l:
                backtrack(curr + ")", l, r + 1)


        backtrack("", 0, 0)
        return res
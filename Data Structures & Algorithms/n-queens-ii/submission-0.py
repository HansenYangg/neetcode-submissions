class Solution:
    def totalNQueens(self, n: int) -> int:
        
        res, seenCol, seenHori, seenVert = 0, set(), set(), set()
        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1 
                return

            if r > n:
                return

            for c in range(n):
                if c not in seenCol and r + c not in seenHori and r - c not in seenVert:
                    seenCol.add(c)
                    seenHori.add(r + c)
                    seenVert.add(r - c)
                    backtrack(r + 1)
                    seenCol.remove(c)
                    seenHori.remove(r + c)
                    seenVert.remove(r - c)

    

        backtrack(0)
        return res

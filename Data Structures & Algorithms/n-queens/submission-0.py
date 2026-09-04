class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # row + col and row - col for diagonals

        # for every row, we insert a queen in position row[i], and then 
        # check to see if it's column has not been seen/used before, as well as
        # it's horizontal and vertical diagonals

        res = []

        def backtrack(arr, seenCol, seenHori, seenVert):

            if len(arr) == n:
                res.append(arr.copy())
                return
            r = len(arr)
            for c in range(n): 
                row = ("." * c) + "Q" + ("." * (n - c - 1))
                if c in seenCol or r + c in seenHori or r - c in seenVert:
                    continue

                seenCol.add(c)
                seenHori.add(r+c)
                seenVert.add(r-c)
                backtrack(arr + [row], seenCol, seenHori, seenVert)
                seenCol.remove(c)
                seenHori.remove(r+c)
                seenVert.remove(r-c)
                
                    
        backtrack([], set(), set(), set())
        

        return res
                
        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(string, r, c, visited):
            if string == word:
                return True
            
            if len(string) >= len(word):
                return 
            # at any pos on the board[i][j], we need to add the char and then recursively backtrack on all 4 possible dirs
            
            
            # backtrack in all 4 dirs
           
            if r < len(board) - 1:
                if (r + 1, c) not in visited:
                    visited.add((r + 1, c))
                    if backtrack(string + board[r+1][c], r + 1, c, visited):
                        return True
                    visited.remove((r + 1, c))
                
                
            if r > 0:
                if (r - 1, c) not in visited:
                    visited.add((r - 1, c))
                    if backtrack(string + board[r-1][c], r - 1, c, visited):
                        return True
                    visited.remove((r - 1, c))
               

            if c < len(board[0]) - 1:
                if (r, c + 1) not in visited:
                    visited.add((r, c + 1))
                    if backtrack(string + board[r][c+1], r, c + 1, visited):
                        return True
                    visited.remove((r, c + 1))
              
            if c > 0:
                if (r, c - 1) not in visited:
                    visited.add((r, c - 1))
                    if backtrack(string + board[r][c-1], r, c - 1, visited):
                        return True
                    visited.remove((r, c - 1))
              

                        

        for r in range(len(board)):
            for c in range(len(board[0])):
                char = board[r][c]
                s = set()
                s.add((r,c))
                if backtrack(char, r, c, s):
                    return True

        return False
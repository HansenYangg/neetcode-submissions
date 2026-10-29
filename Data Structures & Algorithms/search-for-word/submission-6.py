class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        visited = set()

        def backtrack(string, r, c):
            if string == word:
                return True
            
            if len(string) >= len(word):
                return 
            # at any pos on the board[i][j], we need to add the char and then recursively backtrack on all 4 possible dirs
            
            
            # backtrack in all 4 dirs
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    if backtrack(string + board[nr][nc], nr, nc):
                        return True
                    visited.remove((nr, nc))

            return False 

          
              

                    

        for r in range(len(board)):
            for c in range(len(board[0])):
                char = board[r][c]
                visited.add((r, c))
               
                if backtrack(char, r, c):
                    return True

                visited.remove((r, c))

        return False
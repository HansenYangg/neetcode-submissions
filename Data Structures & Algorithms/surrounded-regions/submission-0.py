class Solution:
    def solve(self, board: List[List[str]]) -> None:
        

        visited = set()

        def dfs(r, c, regionIndices):
            found = False
            stack = [(r, c)]

            while stack:

                row, col = stack.pop()
                regionIndices.add((row, col))
                if row == 0 or row == len(board) - 1 or col == 0 or col == len(board[0]) - 1:
                    found = True
                    
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


                for direction in directions:
                    dr, dc = direction
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and (nr, nc) not in visited and board[nr][nc] == "O":
                        visited.add((nr, nc))
                        stack.append((nr, nc))

            return found

            
            

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and (r, c) not in visited:
                    visited.add((r, c))
                    indices = set()
                    ans = dfs(r, c, indices) # return true if found an edge
                   
                    if ans == False:
                        for indice in indices:
                            row, col = indice
                            board[row][col] = "X"




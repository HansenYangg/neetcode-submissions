class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        '''

        for pacific, is valid if r == 0 or c == 0
        for atlantic, is valid if r == len(heights) - 1, or c = len(heights[0]) - 1

        for each node, can dfs the node in the 4 directions, and see if it ever reaches both the pacific and atlantic
        if so, add to result array storing [r, c] sublists


        '''

        res = []


        def dfs(r, c, oceans):
            if r == 0 or c == 0:
                oceans[0] = True

            if r == len(heights) - 1 or c == len(heights[0]) - 1:
                oceans[1] = True
            
            if all(oceans):
                return

            stack = [(r, c)]
            visited = set()
            visited.add((r, c))

            while stack:
                row, col = stack.pop()
                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for direction in dirs:
                    nr, nc = row + direction[0], col + direction[1]
                    if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]) and (nr, nc) not in visited and heights[row][col] >= heights[nr][nc]:
                        visited.add((nr, nc))
                        stack.append((nr, nc))


                        if nr == 0 or nc == 0:
                            oceans[0] = True

                        if nr == len(heights) - 1 or nc == len(heights[0]) - 1:
                            oceans[1] = True
                        
                        if all(oceans):
                            return




        for r in range(len(heights)):
            for c in range(len(heights[0])):
                found_oceans = [False, False] # index 0 for pacific, 1 for atlantic
                dfs(r, c, found_oceans)
                if all(found_oceans):
                    res.append([r, c])


        return res
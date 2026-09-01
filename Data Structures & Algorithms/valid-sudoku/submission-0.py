class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check every row
        
        for row in board: #O(1)
            s = set()
            for element in row: #O(1)
                if element != ".":
                    if element in s:
                        return False
                    s.add(element)
        
        
        # check every col
       
        for c in range(9):
            s = set()
            for r in range(9):
                element = board[r][c]
                if element != ".":
                    if element in s:
                        return False
                    s.add(element)
        
        


        # [ ((0, 3), (0, 3)), ((3, 6), (0, 3)), ((6, 9), (0, 3)),
        #   ((0, 3), (3, 6)), ((3, 6), (3, 6)), ((6, 9)), (3, 6),
        #   ((0, 3), (6, 9)), ((3, 6), (6, 9)), ((6, 9), (6, 9))
        # ]
        # check every 3x3
        three_by_threes = [ ((0, 3), (0, 3)), ((3, 6), (0, 3)), ((6, 9), (0, 3)),
           ((0, 3), (3, 6)), ((3, 6), (3, 6)), ((6, 9), (3, 6)),
           ((0, 3), (6, 9)), ((3, 6), (6, 9)), ((6, 9), (6, 9))
        ]
        
        for rows, cols in three_by_threes:
            print(rows, rows[0], rows[1])
            s = set()
            for r in range(rows[0], rows[1]):
                for c in range(cols[0], cols[1]):
                    element = board[r][c]
                    if element != ".":
                        if element in s:
                            return False
                        s.add(element)
        return True



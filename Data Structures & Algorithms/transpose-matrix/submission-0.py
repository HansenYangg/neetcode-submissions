class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix[0]), len(matrix)
        
        res = [ [0] * c for _ in range(r) ]
        print(res)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                res[j][i] = matrix[i][j]

        return res

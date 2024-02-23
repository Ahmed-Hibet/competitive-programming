class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        transposed_matrix = [[] for i in range(m)]

        for i in range(n):
            for j in range(m):
                transposed_matrix[j].append(matrix[i][j])
        return transposed_matrix

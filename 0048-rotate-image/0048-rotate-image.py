class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        store = list(list(reversed(x)) for x in zip(*matrix))
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = store[i][j]
                
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])

        self.prefix_sum = [[0]*(col+1) for i in range(row+1)]
        for i in range(row):
            for j in range(col):
                self.prefix_sum[i+1][j+1] = self.prefix_sum[i][j+1] + self.prefix_sum[i+1][j]- self.prefix_sum[i][j] + matrix[i][j]
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.prefix_sum[row1][col1] + self.prefix_sum[row2+1][col2+1] - self.prefix_sum[row2+1][col1] - self.prefix_sum[row1][col2+1]
        return result
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
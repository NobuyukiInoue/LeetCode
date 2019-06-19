class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            self.sum = None
            return
        h,w = len(matrix),len(matrix[0])
        self.sum = [[0]*w for i in range(h)]
        for i in range(h):
            tmp = 0
            for j in range(w):
                tmp2 = 0 if i == 0 else self.sum[i - 1][j]
                self.sum[i][j] = tmp+matrix[i][j] + tmp2
                tmp += matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        assert self.sum
        blk1 = 0 if row1 == 0 else self.sum[row1 - 1][col2]
        blk2 = 0 if col1 == 0 else self.sum[row2][col1 - 1]
        blk3 = 0 if row1 == 0 or col1 == 0 else self.sum[row1 - 1][col1 - 1]
        blk4 = self.sum[row2][col2]
        return blk4 - blk1 - blk2 + blk3

"""
#   def __init__(self, matrix: List[List[int]]):
    def __init__(self, matrix):
       self.matrix = matrix

#   def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    def sumRegion(self, row1, col1, row2, col2):
       sum = 0
       for i in range(row1, row2 + 1):
           for j in range(col1, col2 + 1):
               sum += self.matrix[i][j]
       return sum
"""

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

public class NumMatrix_old {
    int[][] matrix;
    public NumMatrix_old(int[][] arg_matrix) {
        matrix = arg_matrix;
    }
    
    public int SumRegion(int row1, int col1, int row2, int col2) {
        int sum = 0;
        for (int i = row1; i < row2 + 1; i++) {
            for (int j = col1; j < col2 + 1; j++) {
                sum += matrix[i][j];
            }
        }

        return sum;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.SumRegion(row1,col1,row2,col2);
 */
 
class NumMatrix {
    int[][] sum;

    public NumMatrix(int[][] arg_matrix) {
        sum = new int[arg_matrix.length][];
        for (int i = 0; i < sum.length; i++) {
            int tmp = 0;
            sum[i] = new int[arg_matrix[i].length];
            for (int j = 0; j < arg_matrix[i].length; j++) {
                int tmp2 = 0;
                if (i != 0)
                    tmp2 = sum[i - 1][j];
                sum[i][j] = tmp + arg_matrix[i][j] + tmp2;
                tmp += arg_matrix[i][j];
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int blk1 = 0;

        if (row1 != 0)
            blk1 = sum[row1-1][col2];

        int blk2 = 0;
        if (col1 != 0)
            blk2 = sum[row2][col1-1];

        int blk3 = 0;
        if (row1 != 0 && col1 != 0)
            blk3 = sum[row1-1][col1-1];

        int blk4 = sum[row2][col2];

        return blk4 - blk1 - blk2 + blk3;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */

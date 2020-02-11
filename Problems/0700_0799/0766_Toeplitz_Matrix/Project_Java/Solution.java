public class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length - 1; i++)
            for (int j = 0; j < matrix[i].length - 1; j++)
                if (matrix[i][j] != matrix[i + 1][j + 1])
                    return false;
        return true;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        int[][] matrix = new int[flds.length][];
        for (int i = 0; i < flds.length; i++) {
            matrix[i] = ml.stringTointArray(flds[i]);
            System.out.println("matrix[" + Integer.toString(i) + "] = " + ml.intArrayToString(matrix[i]));
        }

        long start = System.currentTimeMillis();

        boolean result = isToeplitzMatrix(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

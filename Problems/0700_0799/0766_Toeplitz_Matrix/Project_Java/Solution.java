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
        int[][] matrix = ml.stringToIntIntArray(flds);
         System.out.println("matrix = " + ml.matrixToString(matrix));

        long start = System.currentTimeMillis();

        boolean result = isToeplitzMatrix(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

public class Solution {
    public static int[][] imageSmoother(int[][] M)
    {
        int[][] res = new int[M.length][M[0].length];
        int[][] tem = new int[M.length + 2][M[0].length + 2];

        for (int i = 0; i < M.length * M[0].length; i++)
        {
            tem[i / M[0].length + 1][i % M[0].length + 1] = M[i / M[0].length][i % M[0].length];
        }

        for (int i = 0; i < M.length * M[0].length; i++)
        {
            int row   = i / M[0].length;
            int col   = i % M[0].length;
            int count = 9;
            int sum = tem[row + 1][col + 1] +
                    tem[row + 0][col + 0] +
                    tem[row + 0][col + 1] +
                    tem[row + 0][col + 2] +
                    tem[row + 1][col + 0] +
                    tem[row + 1][col + 2] +
                    tem[row + 2][col + 0] +
                    tem[row + 2][col + 1] +
                    tem[row + 2][col + 2];

            if (row == 0 || col == 0 || row == M.length - 1 || col == M[0].length - 1)
            {
                count = 6;
                if (row == 0 && col == 0)
                {
                    count = 4;
                } else if (row == M.length - 1 && col == M[0].length - 1)
                {
                    count = 4;
                } else if (row == 0 && col == M[0].length - 1)
                {
                    count = 4;
                } else if (row == M.length - 1 && col == 0)
                {
                    count = 4;
                }
            }

            if (M.length == 1 || M[0].length == 1)
            {
                count = 3;
                if (row == 0 || col == 0)
                {
                    if (row == 0 && col == 0)
                    {
                        count = 2;
                    } else if (row == 0 && col == M[0].length - 1)
                    {
                        count = 2;
                    } else if (row == M.length - 1 && col == 0)
                    {
                        count = 2;
                    }
                }
                if (M.length == M[0].length)
                {
                    count = 1;
                }
            }

            res[row][col] = sum / count;
        }

        return res;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        int[][] M = new int[flds.length][];
        for (int i = 0; i < flds.length; i++) {
            M[i] = ml.str_to_int_array(flds[i]);
            System.out.println("nums[" + Integer.toString(i) + "] = " + ml.output_int_array(M[i]));
        }

        long start = System.currentTimeMillis();

        int[][] result = imageSmoother(M);

        long end = System.currentTimeMillis();

        System.out.println();
        for (int i = 0; i < flds.length; i++) {
            System.out.println("result[" + Integer.toString(i) + "] = " + ml.output_int_array(result[i]));
        }

        System.out.println((end - start)  + "ms\n");
    }
}

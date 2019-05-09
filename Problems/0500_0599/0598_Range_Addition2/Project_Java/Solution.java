public class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        if (ops == null || ops.length == 0) {
            return m * n;
        }
        
        int row = Integer.MAX_VALUE, col = Integer.MAX_VALUE;
        for(int[] op : ops) {
            row = Math.min(row, op[0]);
            col = Math.min(col, op[1]);
        }
        
        return row * col;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[[", "").replace("]]]", "").trim().split("\\]\\],\\[\\[");

        String[] m_and_n = flds[0].split("\\],\\[");
        int m = Integer.parseInt(m_and_n[0]);
        int n = Integer.parseInt(m_and_n[1]);
        System.out.println("m = " + Integer.toString(m) + ", n = " + Integer.toString(n));

        int[][] ops;

        if (flds.length < 2) {
            ops = new int[0][];
        } else {
            Mylib ml = new Mylib();
            String[] nums = flds[1].split("\\],\\[");
            ops = new int[nums.length][];
            for (int i = 0; i < nums.length; i++) {
                ops[i] = ml.str_to_int_array(nums[i]);
                System.out.println("ops[" + Integer.toString(i) + "] = " + ml.output_int_array(ops[i]));
            }
        }

        long start = System.currentTimeMillis();

        int result = maxCount(m, n, ops);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

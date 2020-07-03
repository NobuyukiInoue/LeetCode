import java.util.*;

public class Solution {
    public int xorOperation(int n, int start) {
        // 0ms
        int res = start;
        for (int i = 1; i < n; i++)
            res ^= start + 2*i;
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int n     = Integer.parseInt(flds[0]);
        int arg_start = Integer.parseInt(flds[1]);
        System.out.println("n = " +String.valueOf(n) + ", start = " + String.valueOf(arg_start));

        long start = System.currentTimeMillis();

        int result = xorOperation(n, arg_start);

        long end = System.currentTimeMillis();

        System.out.println("result = " + String.valueOf(result));
        System.out.println((end - start)  + "ms\n");
    }
}

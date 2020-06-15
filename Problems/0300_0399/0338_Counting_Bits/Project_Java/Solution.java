import java.util.*;

public class Solution {
    public int[] countBits(int num) {
        // 1ms
        int[] res = new int[num + 1];

        res[0] = 0;
        for (int i = 1; i < num + 1; i++)
            res[i] = res[i>>1] + (i&1);

        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib mc = new Mylib();
        int num = Integer.parseInt(flds);
        System.out.println("num = " + Integer.toString(num));

        long start = System.currentTimeMillis();

        int[] result = countBits(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + mc.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

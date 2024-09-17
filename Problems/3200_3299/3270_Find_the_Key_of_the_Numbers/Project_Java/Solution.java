import java.util.*;

public class Solution {
    public int generateKey(int num1, int num2, int num3) {
        // 1ms
        int ans = 0, dv = 10;
        while (dv < 100000) {
            int d1 = num1%dv;
            int d2 = num2%dv;
            int d3 = num3%dv;
            ans += Math.min(d1, Math.min(d2, d3));
            num1 -= d1;
            num2 -= d2;
            num3 -= d3;
            dv *= 10;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int num1 = Integer.parseInt(flds[0]);
        int num2 = Integer.parseInt(flds[1]);
        int num3 = Integer.parseInt(flds[2]);
        System.out.println("num1 = " + num1 + ", num2 = " + num2 + ", num3 = " + num3);

        long start = System.currentTimeMillis();

        int result = generateKey(num1, num2, num3);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

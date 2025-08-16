import java.util.*;

public class Solution {
    public boolean checkDivisibility(int n) {
        // 0ms
        int v_prd = 1, v_sum = 0, temp_n = n;
        while (temp_n > 0) {
            int m = temp_n%10;
            v_prd *= m;
            v_sum += m;
            temp_n /= 10;
        }
        return n%(v_prd + v_sum) == 0;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + n);

        long start = System.currentTimeMillis();

        boolean result = checkDivisibility(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

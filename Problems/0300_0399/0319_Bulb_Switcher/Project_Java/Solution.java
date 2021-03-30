import java.util.*;

public class Solution {
    int bulbSwitch(int n) {
        // 0ms
        return (int)(Math.sqrt(n));
    }

    int bulbSwitch2(int n) {
        // 0ms
        if (n == 0) {
            return 0;
        }
        int ans = 1;
        for (int i = 2; i * i <= n; i++) {
            ans++;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = bulbSwitch(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

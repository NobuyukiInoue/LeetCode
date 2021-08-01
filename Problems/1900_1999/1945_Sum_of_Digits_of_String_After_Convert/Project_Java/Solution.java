import java.util.*;

public class Solution {
    public int getLucky(String s, int k) {
        // 2ms
        StringBuilder sb = new StringBuilder();
        for (char ch : s.toCharArray()) {
            sb.append(ch - 96);
        }
        String workStr = sb.toString();
        int ans = 0;
        for (int i = 0; i < k; i++) {
            ans = 0;
            for (char ch : workStr.toCharArray()) {
                ans += ch - '0';
            }
            workStr = Integer.toString(ans);
        }
        return ans;
    }

    public int getLucky2(String s, int k) {
        // 1ms
        char[] ch = s.toCharArray();
        int sum = 0;
        for (char c : ch) {
            sum += (c - 'a' + 1)/10 + (c - 'a' + 1)%10;
        }

        while (--k > 0) {
            int t = 0;
            while (sum > 0) {
                t += sum%10;
                sum /= 10;
            }
            sum = t;
        }
        return sum;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0];
        int k = Integer.parseInt(flds[1]);
        System.out.println("s = " + s + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int result = getLucky(s, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

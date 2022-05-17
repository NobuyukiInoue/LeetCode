import java.util.*;

public class Solution {
    public String largestGoodInteger(String num) {
        // 10ms - 16ms
        int ans = 0, cnt = 1;
        for (int i = 1; i < num.length(); i++) {
            if (num.charAt(i) == num.charAt(i-1)) {
                cnt++;
            } else {
                cnt = 1;
            }
            if (cnt == 3) {
                ans = Math.max(ans, num.charAt(i));
            }
        }
        if (ans == 0) {
            return "";
        }
        ans -= '0';
        return(ans + "" + ans + "" + ans);
    }

    public String largestGoodInteger2(String num) {
        // 7ms - 20ms
        int ans = -1;
        for (int i = 2; i < num.length(); ++i) {
            if (num.charAt(i) == num.charAt(i - 1) && num.charAt(i) == num.charAt(i - 2)) {
                ans = Math.max(ans, (int)num.charAt(i) - '0');
            }
        }
        if (ans == -1)
            return "";
        return(ans + "" + ans + "" + ans);
    }

    public void Main(String temp) {
        String num = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("num = " + num);

        long start = System.currentTimeMillis();

        String result = largestGoodInteger(num);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public boolean isBalanced(String num) {
        // 1ms
        int even = 0, odd = 0;
        for (int i = 0; i < num.length(); i++) {
            if (i%2 == 0) {
                even += num.charAt(i) - '0';
            } else {
                odd += num.charAt(i) - '0';
            }
        }
        return even == odd;
    }

    public void Main(String temp) {
        String num= temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("num = \"" + num + "\"");

        long start = System.currentTimeMillis();

        boolean result = isBalanced(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

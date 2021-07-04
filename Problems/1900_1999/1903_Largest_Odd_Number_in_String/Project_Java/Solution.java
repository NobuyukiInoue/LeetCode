import java.util.*;

public class Solution {
    public String largestOddNumber(String num) {
        // 1ms
        int n = num.length();
        for (int i = n - 1; i >= 0; i--) {
        //  if ((int)num.charAt(i) % 2 == 1) {
            if ((num.charAt(i) - '0') % 2 == 1) {
                return num.substring(0, i + 1);
            }
        }
        return "";
    }

    public void Main(String temp) {
        String num = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("num = " + num);

        long start = System.currentTimeMillis();

        String result = largestOddNumber(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public int minMaxDifference(int num) {
        // 1ms
        String num_str = Integer.toString(num);
        int i = 0;
        while (num_str.charAt(i) == '9' && i < num_str.length() - 1) {
            i++;
        }
        return Integer.parseInt(num_str.replace(num_str.charAt(i), '9')) - Integer.parseInt(num_str.replace(num_str.charAt(0), '0'));
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        int num = Integer.parseInt(flds);
        System.out.println("num = " + Integer.toString(num));

        long start = System.currentTimeMillis();

        int result = minMaxDifference(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

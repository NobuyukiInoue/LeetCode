import java.util.*;

public class Solution {
    public String removeTrailingZeros(String num) {
        // 1ms
        int i;
        for (i = num.length() - 1; i >= 0 && num.charAt(i) == '0'; i--);
        return num.substring(0, i + 1);
    }

    public void Main(String temp) {
        String num = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("num = \"" + num + "\"");

        long start = System.currentTimeMillis();

        String result = removeTrailingZeros(num);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}

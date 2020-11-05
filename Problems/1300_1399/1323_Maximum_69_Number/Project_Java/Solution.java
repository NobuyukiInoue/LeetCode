import java.util.*;

public class Solution {
    public int maximum69Number(int num) {
        // 0ms
        char[] chars = Integer.toString(num).toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '6') {
                chars[i] = '9';
                break;
            }
        }
        return Integer.parseInt(new String(chars));
    }

    public int maximum69Number2(int num) {
        // 4ms
        return Integer.valueOf(String.valueOf(num).replaceFirst("6", "9"));
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int num = Integer.parseInt(fld);
        System.out.println("num = " + Integer.toString(num));

        long start = System.currentTimeMillis();

        int result = maximum69Number(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

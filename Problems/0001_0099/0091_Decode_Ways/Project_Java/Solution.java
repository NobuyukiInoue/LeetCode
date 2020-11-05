import java.util.*;

public class Solution {
    public int numDecodings(String s) {
        // 2ms
        if (s.isEmpty() || s.charAt(0) == '0')
            return 0;

		int len_s = s.length();
        int[] results = new int[len_s + 1];
		results[0] = results[1] = 1;

		for (int i = 2; i <= len_s; i++) {
            int first  = Integer.parseInt(s.substring(i - 1, i));
            int second = Integer.parseInt(s.substring(i - 2, i));

            if (first >= 1 && first <= 9)
                results[i] += results[i - 1];
            if (second >= 10 && second <= 26)
                results[i] += results[i - 2];
        }
        return results[len_s];
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = numDecodings(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

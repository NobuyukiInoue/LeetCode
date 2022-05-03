import java.util.*;

public class Solution {
    public int countPrefixes(String[] words, String s) {
        // 1ms
        int ans = 0;
        for (String word : words) {
            if (s.indexOf(word) == 0) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        String[] words = flds[0].split(",");
        String s = flds[1];
        System.out.println("nums = " + ml.stringArrayToString(words) + ", s = " + s);

        long start = System.currentTimeMillis();

        int result = countPrefixes(words, s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

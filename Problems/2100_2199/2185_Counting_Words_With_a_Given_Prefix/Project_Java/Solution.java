import java.util.*;

public class Solution {
    public int prefixCount(String[] words, String pref) {
        // 0ms
        int ans = 0;
        for (String word : words) {
            if (word.startsWith(pref)) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        String[] words = flds[0].split(",");
        String pref = flds[1];
        System.out.println("nums = " + ml.stringArrayToString(words) + ", pref = " + pref);

        long start = System.currentTimeMillis();

        int result = prefixCount(words, pref);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

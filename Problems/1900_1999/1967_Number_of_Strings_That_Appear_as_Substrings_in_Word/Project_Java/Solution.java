import java.util.*;

public class Solution {
    public int numOfStrings(String[] patterns, String word) {
        // 0ms
        int ans = 0;
        for (String pattern : patterns) {
            if (word.contains(pattern)) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String[] patterns = flds[0].split(",");
        String word = flds[1];
        Mylib ml = new Mylib();
        System.out.println("patterns = " + ml.stringArrayToString(patterns) + ", word = " + word);

        long start = System.currentTimeMillis();

        int result = numOfStrings(patterns, word);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

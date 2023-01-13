import java.util.*;

public class Solution {
    public int closetTarget(String[] words, String target, int startIndex) {
        // 1ms
        if (!contains(words, target)) {
            return -1;
        }
        int n = words.length;
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (words[i].equals(target)) {
                ans = Math.min(ans, Math.min(Math.abs(i - startIndex), n - Math.abs(i - startIndex)));
            }
        }
        return ans;
    }

    private Boolean contains(String[] words, String target) {
        for (String word : words) {
            if (word.equals(target)) {
                return true;
            }
        }
        return false;
    }

    public int closetTarget2(String[] words, String target, int startIndex) {
        // 1ms
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i < words.length; i++) {
            if (words[i].equals(target)) {
                int dist = Math.abs(i - startIndex);
                int oppDist = words.length - dist;
                ans = Math.min(ans, Math.min(dist, oppDist));
            }
        }
        return ans == Integer.MAX_VALUE? -1: ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(", ", ",").replace("\"", "").replace("[[", "").replace("]]", "").split("\\],\\[");

        String[] words = flds[0].split(",");
        String target = flds[1];
        int startIndex = Integer.parseInt(flds[2]);

        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words) + ", target = " + target + ", startIndex = " + Integer.toString(startIndex));
        long start = System.currentTimeMillis();

        int result = closetTarget(words, target, startIndex);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

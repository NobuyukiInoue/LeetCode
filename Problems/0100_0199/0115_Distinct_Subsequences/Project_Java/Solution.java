import java.util.*;

public class Solution {
    public int numDistinct(String s, String t) {
        // 1ms
        int[][] arr = new int[256][t.length() + 1];
        int[] cnt = new int[t.length() + 1];
        cnt[0] = 1;
        char c;
        for (int i = 0; i < t.length(); i++ ) {
            c = t.charAt(i);
            arr[c][arr[c][0] + 1] = i + 1;
            arr[c][0]++;
        }
        for (char a: s.toCharArray() ) {
            if (arr[a][0] != 0) {
                for (int i = arr[a][0]; i > 0; i--) {
                    cnt[arr[a][i]] += cnt[arr[a][i] - 1];
                }
            }
        }
        return cnt[t.length()];
    }

    public void Main(String temp) {
        String[] words = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String s = words[0], t = words[1];
        System.out.println("s = " + s + ", t = " + t);

        long start = System.currentTimeMillis();
        
        int result = numDistinct(s, t);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

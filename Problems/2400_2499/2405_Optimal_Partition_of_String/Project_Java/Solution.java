import java.util.*;

public class Solution {
    public int partitionString(String s) {
        // 9ms - 10ms
        int map = 0;
        int ans = 1;
        for (char ch : s.toCharArray()){
            if ((map & (1 << ch)) != 0) {
                ans++;
                map = 0;
            }
            map |= (1 << ch);
        }
        return ans;
    }

    public int partitionString_arr(String s) {
        // 20ms - 26ms
        int ans = 1;
        boolean[] dup = new boolean[26];
        for (char ch : s.toCharArray()) {
            if (dup[ch - 'a']) {
                dup = new boolean[26];
                ans++;
            }
            dup[ch - 'a'] = true;
        }
        return ans;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = partitionString(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

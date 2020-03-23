import java.util.*;

public class Solution {
    public String sortString(String s) {
        // 2ms
        StringBuilder ans = new StringBuilder();
        int[] count = new int[26];

        for (char c : s.toCharArray())
            ++count[c - 'a'];

        while (ans.length() < s.length()) {
            add(count, ans, true);
            add(count, ans, false);
        }
        return ans.toString();
    }

    private void add(int[] cnt, StringBuilder ans, boolean asc) {
        for (int i = 0; i < 26; ++i) {
            int j = asc ? i : 25 - i;
            if (cnt[j]-- > 0)
                ans.append((char)(j + 'a'));
        }
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();
        
        String result = sortString(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public int countKConstraintSubstrings(String s, int k) {
        // 3ms
        int n = s.length();
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int count0 = 0;
            int count1 = 0;
            for (int j = i; j < n; j++) {
                if (s.charAt(j) == '0') {
                    count0++;
                } else {
                    count1++;
                }
                if (count0 <= k || count1 <= k) {
                    ans++;
                }
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0].replace("\"", "");
        int k = Integer.parseInt(flds[1]);
        System.out.println("s = \"" + s + "\", k = " + k);

        long start = System.currentTimeMillis();

        int result = countKConstraintSubstrings(s, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

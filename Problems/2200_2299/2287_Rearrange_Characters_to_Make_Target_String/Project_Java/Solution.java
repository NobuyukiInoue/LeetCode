import java.util.*;

public class Solution {
    public int rearrangeCharacters(String s, String target) {
        // 0ms - 1ms
        int[] cnt1 = new int[26];
        int[] cnt2 = new int[26];
        for (char ch : s.toCharArray()) {
            cnt1[ch - 'a']++;
        }
        for (char ch : target.toCharArray()) {
            cnt2[ch - 'a']++;
        }
        int res = Integer.MAX_VALUE;
        /*
        // 1ms - 2ms
        for (int i = 0; i < target.length(); i++) {
            int idx = target.charAt(i) - 'a';
            res = Math.min(res, cnt1[idx]/cnt2[idx]);
        }
        */
        // 0ms - 1ms
        for (int i = 0; i < cnt1.length; i++) {
            if (cnt2[i] != 0) { 
                res = Math.min(res, cnt1[i] / cnt2[i]);
            }
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").split(",");
        String s = flds[0];
        String target = flds[1];
        System.out.println("s = " + s + ", target = " + target);

        long start = System.currentTimeMillis();

        int result = rearrangeCharacters(s, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

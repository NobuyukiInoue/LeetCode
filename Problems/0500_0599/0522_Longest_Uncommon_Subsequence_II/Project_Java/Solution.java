import java.util.*;

public class Solution {
    public int findLUSlength(String[] strs) {
        // 1ms
        int maxlen = -1;
        for (int i = 0; i < strs.length; i++) {
            int count = 0;
            for (int j = 0; j < strs.length; j++) {
                if (i != j) {
                    if (isSubSequence(strs[i], strs[j]) == false) {
                        count++;
                    } else {
                        break;
                    }
                }
            }
            if (count == strs.length - 1) {
                 maxlen = Math.max(maxlen, strs[i].length());
            }
        }
        return maxlen;
    }

    private boolean isSubSequence(String a, String b){
        int i, j;
        for (i = 0, j = 0; i < a.length() && j < b.length(); j++) {
            if (a.charAt(i) == b.charAt(j)) {
                i++;
            }
        }
        return (i == a.length());
    }

    public void Main(String temp) {
        String[] strs = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        Mylib ml = new Mylib();
        System.out.println("strs = " + ml.stringArrayToString(strs));

        long start = System.currentTimeMillis();

        int result = findLUSlength(strs);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

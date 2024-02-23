import java.util.*;

public class Solution {
    public List<String> getLongestSubsequence(String[] words, int[] groups) {
        // 1ms
        List<String>ans = new ArrayList<>();
        ans.add(words[0]);
        for (int i = 1; i < words.length; i++) {
            if (groups[i] == groups[i - 1]) {
                continue;
            }
            ans.add(words[i]);
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
 
        Mylib ml = new Mylib();
        String[] words = flds[0].split(",");
        int[] groups = ml.stringToIntArray(flds[1]);
        System.out.println("words = " + ml.stringArrayToString(words) + ", groups = " + ml.intArrayToString(groups));

        long start = System.currentTimeMillis();

        List<String> result = getLongestSubsequence(words, groups);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

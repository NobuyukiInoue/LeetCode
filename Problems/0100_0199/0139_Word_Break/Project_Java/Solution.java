import java.util.*;

public class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        // 2ms
        boolean[] dp = new boolean[s.length() + 1];
        int maxLen = 0;
        for (String str : wordDict) {
            maxLen = Math.max(maxLen, str.length());
        }
        for (int end = 1; end < s.length() + 1; end++){
            if(wordDict.contains(s.substring(0, end))) {
                dp[end] = true;
                continue;
            }
            for (int i = end - maxLen > 1 ? end - maxLen:1; i < end; i++) {
                if (dp[i] == true && wordDict.contains(s.substring(i, end))){
                    dp[end] = true;
                    break;
                }
            }
        }
        return dp[s.length()];
    }

    public boolean wordBreak_work(String s, List<String> wordDict) {
        // 9ms
        List<Integer> pos = new ArrayList<>(0);
        pos.add(0);
        for (int i = 0; i < s.length(); i++) {
            for (int j : pos) {
                if (wordDict.contains(s.substring(j, i + 1))) {
                    pos.add(i + 1);
                    break;
                }
            }
        }
        return pos.get(pos.size() - 1) == s.length();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        String s = flds[0];
        List<String> wordDict =  ml.stringArrayToListStringArray(flds[1].split(","));

        System.out.println("s = " + s + ", wordDict = " + ml.listStringArrayToString(wordDict));

        long start = System.currentTimeMillis();

        boolean result = wordBreak(s, wordDict);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public List<List<String>> partition(String s) {
        // 7ms
        List<List<String>> res = new ArrayList<>();
        boolean[][] dp = new boolean[s.length()][s.length()];
        for (int i = 0; i < s.length(); i++) {
            for (int j = 0; j <= i; j++) {
                if (s.charAt(i) == s.charAt(j) && (i - j <= 2 || dp[j + 1][i - 1])) {
                    dp[j][i] = true;
                }
            }
        }
        helper(res, new ArrayList<>(), dp, s, 0);
        return res;
    }
    
    private void helper(List<List<String>> res, List<String> path, boolean[][] dp, String s, int pos) {
        if (pos == s.length()) {
            res.add(new ArrayList<>(path));
            return;
        }
        
        for (int i = pos; i < s.length(); i++) {
            if (dp[pos][i]) {
                path.add(s.substring(pos, i + 1));
                helper(res, path, dp, s, i + 1);
                path.remove(path.size() - 1);
            }
        }
    }

    public List<List<String>> partition2(String s) {
        // 10ms
        List<List<String>> ans = new ArrayList<>();
        dfs(s, ans, new ArrayList<>(), 0);
        return ans;
    }

    private void dfs(String s, List<List<String>> ans, List<String> op, int k) {
        if (k == s.length()) {
            ans.add(op);
            return;
        }
        for (int i = k; i < s.length(); i++) {
            String temp = s.substring(k, i + 1);
            if (isPalindrome(temp)) {
                List<String> newop = new ArrayList<>(op);
                newop.add(temp);
                dfs(s, ans, newop, i + 1);
            }
        }
    }

    private boolean isPalindrome(String s) {
        int start = 0, end = s.length() - 1;
        while (start < end) {
            if (s.charAt(start) != s.charAt(end)) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        List<List<String>> result = partition(s);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listListStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

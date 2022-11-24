import java.util.*;

public class Solution {
    private List<String> result;

    public List<String> wordBreak(String s, List<String> wordDict) {
        // 3ms
        result = new ArrayList<>();
        find(s, 0, s.length() - 1, wordDict, new ArrayList<>());
        return result;
    }

    private void find(String s, int l, int r, List<String> wordDict, List<String> list) {
        if (l > r) {
            java.util.StringJoiner stringJoiner = new java.util.StringJoiner(" ");
            list.forEach(word -> stringJoiner.add(word));
            result.add(stringJoiner.toString());
            return;
        }
        for (int i = l; i <= r; ++i) {
            String substring = s.substring(l, i + 1);
            if (wordDict.contains(substring)) {
                list.add(substring);
                find(s, i + 1, r, wordDict, list);
                list.remove(list.size() - 1);
            }
        }
    }

    public List<String> wordBreak2(String s, List<String> wordDict) {
        // 9ms
        return dfs(s, wordDict, 0);
    }

    private List<String> dfs(String s, List<String> wordDict, int i) {
        if (i == s.length()) {
            return List.of("");
        }
        List<String> ans = new ArrayList<>();
        for (int k = i; k < s.length(); k++) {
            String left = s.substring(i, k + 1);
            if (wordDict.contains(left)) {
                for (String right : dfs(s, wordDict, k + 1)) {
                    if (!right.equals("")) {
                        ans.add(left + " " + right);
                    } else {
                        ans.add(left + right);
                    }
                }
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        String s = flds[0];
        List<String> wordDict =  ml.stringArrayToListStringArray(flds[1].split(","));

        System.out.println("s = " + s + ", wordDict = " + ml.listStringArrayToString(wordDict));

        long start = System.currentTimeMillis();

        List<String> result = wordBreak(s, wordDict);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

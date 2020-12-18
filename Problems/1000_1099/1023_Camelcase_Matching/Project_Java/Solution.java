import java.util.*;

public class Solution {
    public List<Boolean> camelMatch(String[] queries, String pattern) {
        // 0ms
        List<Boolean> res = new ArrayList<>();
        for (String query : queries)
            res.add(isMatch(query, pattern));
        return res;
    }

    private boolean isMatch(String query, String pattern) {
        int i = 0;
        for (char ch: query.toCharArray()) {
            if (i < pattern.length() && ch == pattern.charAt(i)) {
                i++;
            } else if (ch < 'a') {
                return false;
            }
        }
        return i == pattern.length();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String[] queries = flds[0].split(",");
        String pattern = flds[1];

        Mylib ml = new Mylib();
        System.out.println("queries = " + ml.stringArrayToString(queries));
        System.out.println("pattern = " + pattern);

        long start = System.currentTimeMillis();

        List<Boolean> result = camelMatch(queries, pattern);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listBooleanArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

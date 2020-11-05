import java.util.*;

public class Solution {
    public List<String> restoreIpAddresses(String s) {
        // 2ms
        List<String> res = new ArrayList<>();
        if (s == null || s.length() == 0 || s.length() > 12) {
            return res;
        }
        helper(s, res, new StringBuilder(), 0, 0);
        return res;
    }
    
    private void helper(String s, List<String> res, StringBuilder sb, int pos, int count) {
        if (pos == s.length() && count == 3) {
            res.add(sb.toString());
            return;
        }
        if (count > 3) {
            return;
        }
        for (int i = pos; i < s.length(); i++) {
            String t = s.substring(pos, i + 1);
            if (t.length() > 3 || t.length() > 1 && t.charAt(0) == '0' || Integer.valueOf(t) > 255) {
                break;
            }
            int len = sb.length();
            
            sb.append(t);
            if (i + 1 != s.length()) {
                sb.append(".");
                helper(s, res, sb, i + 1, count + 1);
            } else {
                helper(s, res, sb, i + 1, count);
            }
            sb.setLength(len);
        }
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        List<String> result = restoreIpAddresses(s);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

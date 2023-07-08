import java.util.*;

public class Solution {
    public String countAndSay(int n) {
        // 3ms
        if (n == 1)
            return "1";
        String res = countAndSay(n-1);
        StringBuilder ans = new StringBuilder();
        int left = 0, right = 0;
        while (right < res.length()){
            int counter = 0;
            while (right < res.length() && res.charAt(left) == res.charAt(right)){
                counter++;
                right++;
            }
            ans.append(counter);
            ans.append(res.charAt(left));
            left = right;
        }
        return ans.toString();
    }

    public String countAndSay2(int n) {
        // 4ms - 5ms
        if (n == 1) {
            return "1";
        }
        String x = countAndSay(n - 1);
        StringBuilder ans = new StringBuilder();
        char y = x.charAt(0);
        int ct = 1;
        for (int i = 1; i < x.length(); i++) {
            if (x.charAt(i) == y) {
                ct++;
            } else {
                ans.append(Integer.toString(ct));
                ans.append(Character.toString(y));
                y = x.charAt(i);
                ct = 1;
            }
        }
        ans.append(Integer.toString(ct));
        ans.append(Character.toString(y));
        return ans.toString();
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(fld);
        System.out.println("n = " + n);

        long start = System.currentTimeMillis();

        String result = countAndSay(n);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}

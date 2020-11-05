import java.util.*;

public class Solution {
    public String gcdOfStrings(String str1, String str2) {
        // 0ms
        if (str1.length() < str2.length()) {
            return gcdOfStrings(str2, str1);
        } else if (!str1.startsWith(str2)) {
            return "";
        } else if (str2.isEmpty()) {
            return str1;
        } else {
            return gcdOfStrings(str1.substring(str2.length()), str2);
        }
    }

    public String gcdOfStrings2(String str1, String str2) {
        // 22ms
        String d = str1.length() < str2.length() ? str1 : str2;
        int n = d.length();
        for (int i = 1; i <= n; i++) {
            if (n % i != 0)
                continue;
            String sub = d.substring(0, n / i);
            if (str1.replaceAll(sub, "").equals("") && str2.replaceAll(sub, "").equals("")) {
                return sub;
            }
        }
        return "";
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        String str1 = flds[0];
        String str2 = flds[1];

        System.out.println("str1 = " + str1 + ", str2 = " + str2);

        long start = System.currentTimeMillis();

        String result = gcdOfStrings(str1, str2);

        long end = System.currentTimeMillis();

        System.out.println("result = \n" + result);
        System.out.println((end - start)  + "ms\n");
    }
}

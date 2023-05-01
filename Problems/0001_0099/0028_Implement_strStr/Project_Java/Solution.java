import java.util.*;

public class Solution {
    public int strStr(String haystack, String needle) {
        // 1ms
        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            if (haystack.charAt(i) == needle.charAt(0)) {
                Boolean isSame = true;
                for (int j = 1; j < needle.length(); j++) {
                    if (haystack.charAt(i + j) != needle.charAt(j)) {
                        isSame = false;
                        break;
                    }
                }
                if (isSame) {
                    return i;
                }
            }
        }
        return -1;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        String haystack = flds[0];
        String needle = flds[1];
        System.out.println("haystack = " + haystack + ", needle = " + needle);

        long start = System.currentTimeMillis();

        int result = strStr(haystack, needle);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

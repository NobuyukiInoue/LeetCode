import java.util.*;

public class Solution {
    public boolean hasAllCodes(String s, int k) {
        // 156ms - 208ms
        HashSet<String> codes = new HashSet<>();
        for (int i = 0; i < s.length() - k + 1; i++) {
            codes.add(s.substring(i, i + k));
        }
        return codes.size() == (int)Math.pow(2, k);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0];
        int k = Integer.parseInt(flds[1]);
        System.out.println("s = \"" + s + "\", k = " + k);

        long start = System.currentTimeMillis();

        boolean result = hasAllCodes(s, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

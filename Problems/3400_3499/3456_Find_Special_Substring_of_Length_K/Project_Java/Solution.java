import java.util.*;

public class Solution {
    public boolean hasSpecialSubstring(String s, int k) {
        // 1ms
        int count = 1;
        for(int i = 1; i < s.length(); i++){
            if (s.charAt(i) != s.charAt(i - 1) && count == k) {
                return true;
            }
            if (s.charAt(i) != s.charAt(i - 1)) {
                count = 0;
            }
            count++;
        }
        return (count == k);
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        String s = flds[0];
        int k = Integer.parseInt(flds[1]);
        System.out.println("s = \"" + s + "\", k = " + k);

        long start = System.currentTimeMillis();

        boolean result = hasSpecialSubstring(s, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

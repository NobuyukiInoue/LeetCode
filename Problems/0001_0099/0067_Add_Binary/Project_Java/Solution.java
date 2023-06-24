import java.util.*;

public class Solution {
    public String addBinary(String a, String b) {
        // 3ms
        String ans = "";
        int carry = 0;
        int i = a.length() - 1;
        int j = b.length() - 1;
        while ((i >= 0) || (j >= 0) || carry != 0) {
            if (i >= 0) {
                carry += a.charAt(i--) - '0';
            }
            if (j >= 0) {
                carry += b.charAt(j--) - '0';
            }
            ans = Character.toString(carry % 2 + '0') + ans;
            carry /= 2;
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        String a = flds[0], b = flds[1];
        System.out.println("a = \"" + a + "\", b = \"" + b + "\"");

        long start = System.currentTimeMillis();

        String result = addBinary(a, b);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}

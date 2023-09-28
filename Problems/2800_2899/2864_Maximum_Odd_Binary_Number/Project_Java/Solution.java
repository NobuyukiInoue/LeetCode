import java.util.*;

public class Solution {
    public String maximumOddBinaryNumber(String s) {
        // 2ms
        int oneCount = -1;
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < s.length(); ++i) {
            oneCount += (s.charAt(i) == '1') ? 1 : 0;
        }
        for (int i = 0; i < s.length(); i++, oneCount--) {
            ans.append(oneCount > 0 ? '1' : '0');
        }
        ans.deleteCharAt(ans.length() - 1);
        return ans.append('1').toString();
    }

    public String maximumOddBinaryNumber2(String s) {
        // 7ms
        int ones = 0, zeroes = 0;
        for (char ch : s.toCharArray()) {
            if (ch == '1') ones++;
            else zeroes++;
        }
        return "1".repeat(ones - 1) + "0".repeat(zeroes) + (ones > 0 ? "1" : "");
    }

    public String maximumOddBinaryNumber3(String s) {
        // 14ms
        int cnts = count(s, '1');
        System.out.println("cnts = " + cnts);
        return repeat("1", cnts - 1) + repeat("0", s.length() - cnts) + "1";
    }

    private static int count(String s, char ch) {
        int counter = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ch) {
                counter++;
            }
        }
        return counter;
    }

    private String repeat(String str, int n) {
        StringBuilder sb = new StringBuilder();
        while (n-- > 0) {
            sb.append(str);
        }
        return sb.toString();
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        String result = maximumOddBinaryNumber(s);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}

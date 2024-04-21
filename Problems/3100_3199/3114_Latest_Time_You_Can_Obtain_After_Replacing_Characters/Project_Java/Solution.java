import java.util.*;

public class Solution {
    public String findLatestTime(String s) {
        // 1ms
        char[] arr_s = s.toCharArray();
        if (arr_s[0] == '?') {
            arr_s[0] = (arr_s[1] == '?' || arr_s[1] <= '1') ? '1'  : '0';
        }
        if (arr_s[1] == '?') {
            arr_s[1] = arr_s[0] == '1' ? '1' :'9';
        }
        if (arr_s[3] == '?') {
            arr_s[3] = '5';
        }
        if (arr_s[4] == '?') {
            arr_s[4] = '9';
        }
        return String.valueOf(arr_s);
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        String result = findLatestTime(s);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public String makeSmallestPalindrome(String s) {
        // 10ms
        char[] arr_s = s.toCharArray();
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (arr_s[left] < arr_s[right]) {
                arr_s[right] = arr_s[left];
            } else if (arr_s[left] > arr_s[right]) {
                arr_s[left] = arr_s[right];
            }
            left++;
            right--;
        }
        return new String(arr_s);
    }

    public String makeSmallestPalindrome2(String s) {
        // 11ms
        char[] arr_s = s.toCharArray();
        int len_s = s.length();
        for (int i = 0; i < len_s/2; i++) {
            if (arr_s[i] < arr_s[len_s - i - 1]) {
                arr_s[len_s - i - 1] = arr_s[i];
            } else if (arr_s[i] > arr_s[len_s - i - 1]) {
                arr_s[i] = arr_s[len_s - i - 1];
            }
        }
        return new String(arr_s);
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        String result = makeSmallestPalindrome(s);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}

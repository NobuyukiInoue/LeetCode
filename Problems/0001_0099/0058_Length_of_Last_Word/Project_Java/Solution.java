import java.util.*;

public class Solution {
    public int lengthOfLastWord(String s) {
        // 0ms
        s = s.trim();
        int i = s.length() - 1;
        while (i >= 0 && s.charAt(i) != ' ') {
            i--;
        }
        return s.length() - 1 - i;
    }

    public int lengthOfLastWord2(String s) {
        // 1ms
        s = s.trim();
        String[] arr = s.split(" ");
        return arr[arr.length - 1].length();
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace("[", "").replace("]", "");
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        int result = lengthOfLastWord(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

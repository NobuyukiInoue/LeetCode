import java.util.*;

public class Solution {
    public String modifyString(String s) {
        //  1ms
        char[] arr = s.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == '?') {
                for (int j = 0; j < 3; j++) {
                    if (i > 0 && arr[i - 1] - 'a' == j)
                        continue;
                    if (i + 1 < arr.length && arr[i + 1] - 'a' == j)
                        continue;
                    arr[i] = (char) ('a' + j);
                    break;
                }
            }
        }
        return String.valueOf(arr);
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        String result = modifyString(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public int splitNum(int num) {
        // 1ms
        char[] ca = Integer.toString(num).toCharArray();
        Arrays.sort(ca);
        int[] arr = {0, 0};
        for (int i = 0; i < ca.length; ++i) {
            arr[i % 2] *= 10;
            arr[i % 2] += ca[i] - '0';
        }
        return arr[0] + arr[1];
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        int num = Integer.parseInt(flds);
        System.out.println("num = " + Integer.toString(num));

        long start = System.currentTimeMillis();

        int result = splitNum(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public int largestInteger(int num) {
        // 1ms
        PriorityQueue<Integer> even = new  PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> odd  = new PriorityQueue<>(Collections.reverseOrder());
        char[] arr = Integer.toString(num).toCharArray();
        for (char n : arr) {
            if ((n - 0x30) % 2 == 1) {
                odd.add(n - 0x30);
            } else {
                even.add(n - 0x30);
            }
        }
        int res = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % 2 == 1) {
                res = res*10 + odd.poll();
            } else {
                res = res*10 + even.poll();
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        int num = Integer.parseInt(flds);
        System.out.println("num = " + Integer.toString(num));

        long start = System.currentTimeMillis();

        int result = largestInteger(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

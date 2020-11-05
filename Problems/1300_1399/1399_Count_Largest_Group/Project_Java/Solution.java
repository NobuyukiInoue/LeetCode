import java.util.*;

public class Solution {
    public int countLargestGroup(int n) {
        // 9ms
        int res = 0, max = 0;
        Map<Integer, Integer> count = new HashMap<>();
        for (int i = 1; i <= n; ++i) {
            int sum = 0, j = i;
            while (j > 0) {
                sum += j % 10;
                j /= 10;
            }
            count.put(sum, 1 + count.getOrDefault(sum, 0));
            if (max < count.get(sum)) {
                max = count.get(sum);
                res = 1;
            } else if (max == count.get(sum)) {
                ++res;
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = countLargestGroup(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

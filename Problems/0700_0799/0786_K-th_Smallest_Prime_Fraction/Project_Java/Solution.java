import java.util.*;

public class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        // 3ms
        double lo = 0.0, hi = 1.0;
        while (lo < hi) {
            double mid = (lo + hi) / 2.0;
            int count = 0;
            int[] best = new int[] {0, 1};
            int left = 0;
            for (int right = 1; right < arr.length; right++) {
                while (arr[left] < mid*arr[right]) {
                    left++;
                }
                count += left;
                if (left > 0 && best[0]*arr[right] < best[1]*arr[left - 1]) {
                    best = new int[] {arr[left - 1], arr[right]};
                }
            }
            if (count == k) {
                return best;
            } else if (count > k) {
                hi = mid;
            } else {
                lo = mid;
            }
        }
        return new int[] {0, 0};
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] prices = ml.stringToIntArray(flds[0]);
        int money = Integer.parseInt(flds[1]);
        System.out.println("prices = " + ml.intArrayToString(prices) + ", money = " + money);
 
        long start = System.currentTimeMillis();

        int[] result = kthSmallestPrimeFraction(prices, money);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

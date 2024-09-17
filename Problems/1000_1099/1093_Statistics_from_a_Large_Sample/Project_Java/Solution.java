import java.util.*;

public class Solution {
    public double[] sampleStats(int[] count) {
        // 1ms
        int v_min = -1, v_max = -1;
        int n = 0;
        long v_sum = 0;
        int v_maxcnt = 0, mode = 0;
        for (int i = 0; i < count.length; i++) {
            int cur = count[i];
            if (count[i] == 0) {
                continue;
            }
            if (v_min == -1) {
                v_min = i;
            }
            v_max = Math.max(v_max, i);
            n += cur;
            v_sum += (long)i*count[i];
            if (count[i] > v_maxcnt) {
                v_maxcnt = cur;
                mode = i;
            }
        }
        double median;
        if (n%2 == 1) {
            median = kth(count, n/2 + 1);
        } else {
            median = (kth(count, n/2) + kth(count, n/2 + 1))/2.0;
        }
        return new double[] {v_min, v_max, (double)v_sum/n, median, mode};
    }

    private int kth(int[] count, int k) {
        for (int i = 0; i < count.length; i++) {
            k -= count[i];
            if (k <= 0) {
                return i;
            }
        }
        return 0;
    }

    public String doubeArrayToString(double[] nums) {
        if (nums == null)
            return "[]";
        if (nums.length <= 0)
            return "[]";

        StringBuilder resultStr = new StringBuilder("[" + Double.toString(nums[0]));
        for (int i = 1; i < nums.length; ++i)
            resultStr.append(", " + Double.toString(nums[i]));
        resultStr.append("]");

        return resultStr.toString();
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] count = ml.stringToIntArray(flds);
        System.out.println("counts = " + ml.intArrayToString(count));

        long start = System.currentTimeMillis();

        double[] result = sampleStats(count);

        long end = System.currentTimeMillis();

        System.out.println("result = " + doubeArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

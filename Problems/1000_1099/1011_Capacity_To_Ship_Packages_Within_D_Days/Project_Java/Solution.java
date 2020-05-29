import java.util.*;

public class Solution {
    public int shipWithinDays(int[] weights, int D) {
        // 5ms
        int maxWeight = intArrayMax(weights);
        int lo = intArraySum(weights) / D;
        int hi = maxWeight*weights.length / D + 1;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (mid < maxWeight || !canShip(weights, mid, D)) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

    private boolean canShip(int[] weights, int capacity, int D) {
        int count = 1;
        int loaded = 0; 
        for (int w : weights) {
            if (loaded + w <= capacity) {
                loaded += w;
            } else {
                count++;
                loaded = w;
            }
        }
        if  (count <= D) {
            return true;
        } else {
            return false;
        }
    }

    private int intArrayMax(int[] data) {
        if (data.length <= 0)
            return 0;

        int max = data[0];
        for (int i = 1; i < data.length; i++)
            if (data[i] > max)
                max = data[i];
        return max;
    }

    private int intArraySum(int[] data) {
        if (data.length <= 0)
            return 0;

        int sum = data[0];
        for (int i = 1; i < data.length; i++)
            sum += data[i];
        return sum;
    }

    public int shipWithinDays2(int[] weights, int D) {
        // 8ms
        int left = 0, right = 0;
        for (int w: weights) {
            left = Math.max(left, w);
            right += w;
        }
        while (left < right) {
            int mid = (left + right) / 2, need = 1, cur = 0;
            for (int w: weights) {
                if (cur + w > mid) {
                    need += 1;
                    cur = 0;
                }
                cur += w;
            }
            if (need > D) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] weights = mc.stringTointArray(flds[0]);
        int D = Integer.parseInt(flds[1]);

        System.out.println("weights = " + mc.intArrayToString(weights));
        System.out.println("D = " + String.valueOf(D));

        long start = System.currentTimeMillis();
        
        int result = shipWithinDays(weights, D);

        long end = System.currentTimeMillis();

        System.out.println("result = " + String.valueOf(result));
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public int countRangeSum(int[] nums, int lower, int upper) {
        // 10ms
        if (lower > upper || nums == null || nums.length == 0) {
            return 0;
        }
        int n = nums.length;
        long[] sums = new long[n + 1];
        for (int i = 1; i <= n; ++i) {
            sums[i] = nums[i - 1] + sums[i - 1];
        }
        return mergeSortAndCount(sums, 0, n, lower, upper);
    }

    private int mergeSortAndCount(long[] sums, int l, int r, int lower, int upper) {
        if (l >= r) {
            return 0;
        }
        int m = l + (r - l) / 2;
        int cnt = mergeSortAndCount(sums, l, m, lower, upper) + mergeSortAndCount(sums, m + 1, r, lower, upper);
        int i = m + 1;
        int j = m + 1;
        for (int k = l; k <= m; ++k) {
            while (i <= r && sums[i] - sums[k] < lower) {
                ++i;
            }
            while (j <= r && sums[j] - sums[k] <= upper) {
                ++j;
            }
            cnt += j - i;
        }
        merge(sums, l, r);
        return cnt;
    }

    private void merge(long[] sums, int l, int r) {
        int m = l + (r - l) / 2;
        long[] tmp = new long[r - l + 1];
        int i = l;
        int j = m + 1;
        for (int k = 0; k < tmp.length; ++k) {
            if (i <= m && j <= r) {
                if (sums[i] < sums[j]) {
                    tmp[k] = sums[i++];
                } else {
                    tmp[k] = sums[j++];
                }
            } else if (i <= m) {
                tmp[k] = sums[i++];
            } else {
                tmp[k] = sums[j++];
            }
        }
        System.arraycopy(tmp, 0, sums, l, r - l + 1);
    }

    public int countRangeSum2(int[] nums, int lower, int upper) {
        // 38ms
        int count = 0;
        long[] sum = new long[nums.length + 1];
        TreeMap<Long, Integer> map = new TreeMap<Long, Integer>(); 
        map.put(0L, 1);
        for(int i = 0; i < nums.length; i++){
            sum[i + 1] = sum[i] + nums[i];
            map.put(sum[i + 1], map.containsKey(sum[i + 1])? map.get(sum[i + 1]) + 1: 1);
        }
        for(int i = 0; i < nums.length; i++){
            map.put(sum[i], map.get(sum[i]) - 1);
            if (map.get(sum[i]) == 0)
                map.remove(sum[i]);
            for (Map.Entry<Long, Integer> entry: map.subMap(sum[i] + lower, sum[i] + upper + 1).entrySet())
                count += entry.getValue();
        }
        return count;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int lower = Integer.parseInt(flds[1]);
        int upper = Integer.parseInt(flds[2]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", lower = " + lower + ", upper = " + upper);

        long start = System.currentTimeMillis();

        int result = countRangeSum(nums, lower, upper);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public int splitArray(int[] nums, int m) {
        // 1ms
        int start = 0, end = 0;
        for (int num : nums) {
            start = Math.max(start, num);
            end += num;
        }
        while (start < end) {
            int mid = start + (end - start)/2;
            int total = 0, pieces = 1;
            for (int num : nums) {
                if (total + num > mid) {
                    total = num;
                    pieces++;
                } else {
                    total += num;
                }
            }
            if (pieces > m) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return end;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int m = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + Integer.toString(m));

        long start = System.currentTimeMillis();

        int result = splitArray(nums, m);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

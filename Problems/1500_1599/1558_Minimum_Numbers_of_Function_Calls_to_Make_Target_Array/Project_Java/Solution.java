import java.util.*;

public class Solution {
    /*
    private void modity(int[] arr, int op, int idx) {
        // add by 1 index idx
        if (op == 0) {
            arr[idx]++;
        }
        // multiply by 2 all elements
        if (op == 1) {
            for (int i = 0; i < arr.length; i++) {
                arr[i] *= 2;
            }
        }
    }
    */

    public int minOperations(int[] nums) {
        // 5ms
        int cntAdd = 0, cntDbl = 0, tmp = 0;
        for (int num : nums) {
            if (num != 0) {
                cntAdd++;
            }
            tmp = 0;
            while (num > 1) {
                cntAdd += num&1;
                tmp++;
                num >>= 1;
            }
            cntDbl = Math.max(tmp,cntDbl);
        }
        return cntDbl + cntAdd;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = minOperations(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        // 10ms
        int[] idx = new int[primes.length];
        int[] nums = new int[n];
        nums[0] = 1;
        int ctr = 1;
        while (ctr < n) {
            int min = Integer.MAX_VALUE;
            for(int i = 0; i < primes.length; i++) {
                int t = nums[idx[i]] * primes[i];
                if(t <= nums[ctr-1]) {
                    idx[i]++;
                    t = nums[idx[i]] * primes[i];
                }
                min = Math.min(min, t);
            }
            nums[ctr] = min;
            ctr++;
        }
        return nums[n-1];
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int n = Integer.parseInt(flds[0]);
        int[] primes = ml.stringTointArray(flds[1]);

        System.out.println("n = " + Integer.toString(n));
        System.out.println("primes = " + ml.intArrayToString(primes));

        long start = System.currentTimeMillis();

        int result = nthSuperUglyNumber(n, primes);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

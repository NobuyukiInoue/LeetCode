import java.util.*;

public class Solution {
    public int getMaximumGenerated(int n) {
        // 0ms
        if (n < 1)
            return 0;

        int nums[] = new int[n + 1];
        nums[0] = 0;
        nums[1] = 1;
        int max_num = 1;
        for (int i = 1;i <= n; i++) {
            if (2 * i <= n){
                nums[2*i] = nums[i];
                max_num = Math.max(max_num, nums[2*i]);
            }  
            if(((2 * i) + 1) <= n){
                nums[(2*i)+1] = nums[i] + nums[i + 1];
                max_num = Math.max(max_num, nums[(2*i) + 1]);
            }
        }
        return max_num;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = getMaximumGenerated(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

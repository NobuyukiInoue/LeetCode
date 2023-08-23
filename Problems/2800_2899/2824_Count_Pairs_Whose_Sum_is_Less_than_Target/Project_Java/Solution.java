import java.util.*;

public class Solution {
    public int countPairs(List<Integer> nums, int target) {
        // 3ms
        int n = nums.size();
        int ans = 0;
        Collections.sort(nums);
        for (int i = 0; i < n - 1; i++) {
            int nums_i = nums.get(i);
            for (int j = i + 1; j < n; j++) {
                if (nums_i + nums.get(j) >= target) {
                    break;
                }
            ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        List<Integer> numss = ml.stringToListIntArray(flds[0]);
        int target = Integer.parseInt(flds[1]);
        System.out.println("numss = " + ml.listIntArrayToString(numss) + ", target = " + target);
 
        long start = System.currentTimeMillis();

        int result = countPairs(numss, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

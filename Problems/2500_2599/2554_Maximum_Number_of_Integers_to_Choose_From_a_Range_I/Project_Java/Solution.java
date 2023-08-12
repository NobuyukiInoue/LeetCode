import java.util.*;

public class Solution {
    public int maxCount(int[] banned, int n, int maxSum) {
        // 46ms - 47ms
        Set<Integer>set=new HashSet<>();
        for (int i = 0; i < banned.length; i++) {
            set.add(banned[i]);
        }
        int ans = 0, total = 0;
        for (int i = 1; i < n + 1; i++) {
            if (total + i > maxSum) {
                break;
            }
            if (!set.contains(i)){
                ans++;
                total += i;
            }
        }
        return ans;
    }

    public int maxCount2(int[] banned, int n, int maxSum) {
        // 1163ms - 1188ms
        int ans = 0, total = 0;
        for (int i = 1; i < n + 1; i++) {
            if (total + i > maxSum) {
                break;
            }
            if (!contains(banned, i)) {
                total += i;
                ans++;
            }
        }
        return ans;
    }

    private boolean contains(int[] nums, int target) {
        for (int num : nums) {
            if (num == target) {
                return true;
            }
        }
        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] banned = ml.stringToIntArray(flds[0]);
        int n = Integer.parseInt(flds[1]);
        int maxSum = Integer.parseInt(flds[2]);
        System.out.println("banned = " + ml.intArrayToString(banned) + ", n = " + n + ", maxSum = " + maxSum);
 
        long start = System.currentTimeMillis();

        int result = maxCount(banned, n, maxSum);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

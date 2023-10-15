import java.util.*;

public class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        // 16ms - 17ms
        int m = l.length;
        List<Boolean> ans = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            int[] temp = Arrays.copyOfRange(nums, l[i], r[i] + 1);
            Arrays.sort(temp);
            ans.add(checkDiff(temp));
        }
        return ans;
    }

    private Boolean checkDiff(int[] temp) {
        int diff = temp[1] - temp[0];
        for (int i = 2; i < temp.length; i++) {
            if (temp[i] - temp[i - 1] != diff) {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int[] l = ml.stringToIntArray(flds[1]);
        int[] r = ml.stringToIntArray(flds[2]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", l = " + ml.intArrayToString(l) + ", r = " + ml.intArrayToString(r));

        long start = System.currentTimeMillis();

        List<Boolean> result = checkArithmeticSubarrays(nums, l, r);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

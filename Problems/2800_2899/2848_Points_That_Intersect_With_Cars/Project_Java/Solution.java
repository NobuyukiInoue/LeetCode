import java.util.*;

public class Solution {
    public int numberOfPoints(List<List<Integer>> nums) {
        // 5ms
        Set<Integer> lst = new HashSet<>();
        for (List<Integer> cur : nums) {
            for (int i = cur.get(0); i <= cur.get(1); i++) {
                lst.add(i);
            }
        }
        return lst.size();
    }

    public int numberOfPoints2(List<List<Integer>> nums) {
        // 1ms - 2ms
        boolean[] lst = new boolean[101];
        for (List<Integer> range: nums) {
            int start = range.get(0);
            int end = range.get(1);
            for (int i = start; i <= end; i++) {
                lst[i] = true;
            }
        }
        int ans = 0;
        for (int i = 0; i < lst.length; i++) {
            if (lst[i]) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        List<List<Integer>> nums = ml.stringArrayToListListIntArray(str_mat);
        System.out.println("nums = " + ml.listListIntArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = numberOfPoints(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

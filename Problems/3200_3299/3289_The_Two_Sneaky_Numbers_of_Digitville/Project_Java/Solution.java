import java.util.*;

public class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        // 3ms
        HashMap<Integer, Integer> cnts = new HashMap<>();
        List<Integer> lists = new ArrayList<>();
        for (int num : nums) {
            cnts.put(num, cnts.getOrDefault(num, 0) + 1);
            if (cnts.get(num) == 2) {
                lists.add(num);
            }
        }
        int[] ans = new int[lists.size()];
        for (int i = 0; i < lists.size(); i++) {
            ans[i] = lists.get(i);
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = getSneakyNumbers(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

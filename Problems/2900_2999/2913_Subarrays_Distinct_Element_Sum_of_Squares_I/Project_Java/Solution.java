import java.util.*;

public class Solution {
    public int sumCounts(List<Integer> nums) {
        // 7ms
        int m = nums.size(), ans = 0;
        HashSet<Integer> hs;
        for (int i = 0; i < m; i++) {
            hs = new HashSet<>();
            for (int j = i; j < m; j++) {
                hs.add(nums.get(j));
                ans += hs.size()*hs.size();
            }
        }
        return ans;
    }

    public int sumCounts2(List<Integer> nums) {
        // 92ms - 93ms
        Map<Integer, Integer> mp = new HashMap<>();
        int ans = 0;
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i; j < nums.size(); j++) {
                for (int k = i; k <= j; k++) {
                    mp.put(nums.get(k), 0);
                }
                ans += mp.size()*mp.size();
                mp.clear();
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        List<Integer> nums = ml.stringToListIntArray(flds);
        System.out.println("nums = " + ml.listIntArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = sumCounts(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

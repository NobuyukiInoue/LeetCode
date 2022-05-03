import java.util.*;

public class Solution {
    public List<Integer> intersection(int[][] nums) {
        // 5ms - 11ms
        Map<Integer, Integer> countMap = new HashMap<>();
        List<Integer> inEachArray = new ArrayList<>();
        for (int[] num : nums) {
            for (int x : num) {
                countMap.put(x, countMap.getOrDefault(x, 0) + 1);
                if (countMap.get(x) == nums.length) {
                    inEachArray.add(x);
                }
            }
        }
        inEachArray.sort(Comparator.naturalOrder());
        return inEachArray;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] nums = ml.stringToIntIntArray(str_mat);
        System.out.println("nums = " + ml.intIntArrayToString(nums));

        long start = System.currentTimeMillis();

        List<Integer> result = intersection(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

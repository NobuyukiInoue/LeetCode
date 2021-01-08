import java.util.*;

public class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        // 24ms
        HashMap<Integer, Integer> dic = new HashMap<>();
        for (int n : nums) {
            dic.put(n, dic.getOrDefault(n, 0) + 1);
        }
        List<Integer> res = new ArrayList<>();
        for (Integer key : dic.keySet()) {
            if (dic.get(key) > 1)
                res.add(key);
        }
        
        Collections.sort(res);
        return res;
    }

    public List<Integer> findDuplicates2(int[] nums) {
        // 16ms
        List<Integer> res = new ArrayList<>();;
        Arrays.sort(nums);
    
        for(int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1])
                res.add(nums[i]);
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        List<Integer> result = findDuplicates(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

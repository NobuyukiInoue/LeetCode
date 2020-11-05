import java.util.*;

public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        // 1ms
        List<List<Integer>> res = new ArrayList<>();
        for (int n : nums) {
            if (res.size() == 0) {
                res.add(new ArrayList<>(Arrays.asList(n)));
            } else {
                List<List<Integer>> newRes = new ArrayList<>();
                for (int i = 0; i < res.size(); i++) {
                    List<Integer> memo = res.get(i);
                    for (int j = 0; j <= memo.size(); j++) {
                        List<Integer> temp = new ArrayList<>(memo);
                        temp.add(j, n);
                        newRes.add(temp);
                    }
                }
                res = newRes;
            }
        }

        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        List<List<Integer>> result = permute(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

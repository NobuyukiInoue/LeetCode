import java.util.*;

import javax.lang.model.util.ElementScanner6;

public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        // 0ms
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        res.add(new ArrayList<Integer>());
        for (int n : nums) {
            int lastSize = res.size();
            for (int i = 0; i < lastSize; i++) {
                List<Integer> temp = new ArrayList<>(res.get(i));
                temp.add(n);
                res.add(temp);
            }
        }
        return res;
    }

    public List<List<Integer>> subsets2(int[] nums) {
        // 0ms
        List<List<Integer>> subsets = new ArrayList<>();
        subsets.add(new ArrayList<>());
        findSubsets(nums, 0, subsets);
        return subsets;
    }
    
    private void findSubsets(int[] nums, int index, List<List<Integer>> subsets) {
        if (index >= nums.length) return;
        int size = subsets.size();
        for (int i = 0; i < size; i++) {
            List<Integer> newList = new ArrayList<>(subsets.get(i));
            newList.add(nums[index]);
            subsets.add(newList);
        }
        findSubsets(nums, index + 1, subsets);
    }

    public List<List<Integer>> subsets3(int[] nums) {
        // 0ms
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subset = new ArrayList<Integer>();
        for (int i = 0, j = -1; i < 1 << nums.length; i++, res.add(subset), subset = new ArrayList<Integer>(), j = -1)
            while (++j < nums.length)
                if (((1 << j) & i) == (1 << j))
                    subset.add(nums[j]);
        return res;
    }


    public String listListArrayToString(List<List<Integer>> list) {
        if (list.size() <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[" + listArrayToString(list.get(0)));
        for (int i = 1; i < list.size(); i++) {
            sb.append("," + listArrayToString(list.get(i)));
        }

        sb.append("]");
        return sb.toString();
    }

    public String listArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";
        StringBuilder sb = new StringBuilder("[" + Integer.toString(list.get(0)));
        for (int i = 1; i < list.size(); i++) {
            sb.append("," + Integer.toString(list.get(i)));
        }
        sb.append("]");
        return sb.toString();
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringTointArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        List<List<Integer>> result = subsets(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listListArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

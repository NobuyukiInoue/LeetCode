import java.util.*;

public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        // 0ms
        List<List<Integer>> result = new ArrayList<>();
        permuteUnique(result, nums, 0);
        return result;
    }

    private void permuteUnique(List<List<Integer>> result, int[] nums, int idx) {
        if (idx == nums.length) {
            ArrayList<Integer> arrayList = new ArrayList<>();
            for (int num : nums) {
                arrayList.add(num);
            }
            result.add(arrayList);
        }
        for (int i = idx; i < nums.length; i++) {
            if (!isDuplicate(nums, idx, i)) {
                swap(nums, idx, i);
                permuteUnique(result, nums, idx + 1);
                swap(nums, idx, i);
            }
        }
    }

    private boolean isDuplicate(int[] nums, int idx, int i) {
        for (int i1 = idx; i1 < i; i1++) {
            if (nums[i1] == nums[i]) {
                return true;
            }
        }
        return false;
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    public String intArrayToString(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";
            result += Integer.toString(data[i]);
        }
    
        return result;
    }

    private String listlistIntToString(List<List<Integer>> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + listIntArrayToString(list.get(0));
        for (int i = 1; i < list.size(); i++) {
            resultStr += "," + listIntArrayToString(list.get(i));
        }

        return resultStr + "]";
    }

    public String listIntArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (int i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.str_to_int_array(flds);
        System.out.println("nums = " + intArrayToString(nums));

        long start = System.currentTimeMillis();
        
        List<List<Integer>> result = permuteUnique(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listlistIntToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

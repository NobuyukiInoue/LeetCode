import java.util.*;

public class Solution {
    public List<Integer> majorityElement2(int[] nums) {
        // 9ms
        List<Integer> res = new ArrayList<>();
        int limit = nums.length / 3;
        Map<Integer, Integer> map = new HashMap<>();
    	for (int target : nums) {
            int val;
            if (map.containsKey(target)) {
                val = map.get(target) + 1;
            } else {
                val = 1;
            }
            map.put(target, val);

            if (val > limit) {
                if (res.contains(target) == false) {
                    res.add(target);
                }
            }
        }
        return res;
    }

    public List<Integer> majorityElement(int[] nums) {
        // 1ms
        if (nums == null || nums.length == 0)
            return new ArrayList<Integer>();
        List<Integer> result = new ArrayList<Integer>();
        int number1 = nums[0], number2 = nums[0], count1 = 0, count2 = 0, len = nums.length;
        for (int i = 0; i < len; i++) {
            if (nums[i] == number1)
                count1++;
            else if (nums[i] == number2)
                count2++;
            else if (count1 == 0) {
                number1 = nums[i];
                count1 = 1;
            } else if (count2 == 0) {
                number2 = nums[i];
                count2 = 1;
            } else {
                count1--;
                count2--;
            }
        }
        count1 = 0;
        count2 = 0;
        for (int i = 0; i < len; i++) {
            if (nums[i] == number1)
                count1++;
            else if (nums[i] == number2)
                count2++;
        }
        if (count1 > len / 3)
            result.add(number1);
        if (count2 > len / 3)
            result.add(number2);
        return result;
    }

    public String listIntArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib mc = new Mylib();
        int[] nums = mc.stringTointArray(flds);

        System.out.println("nums = " + mc.intArrayToString(nums));

        long start = System.currentTimeMillis();

        List<Integer> result = majorityElement(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

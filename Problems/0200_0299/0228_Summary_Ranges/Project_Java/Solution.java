import java.util.*;

public class Solution {
    public List<String> summaryRanges(int[] nums) {
        // 0ms
        List<String> out = new ArrayList<String>();
        int i = 0;
        while (i < nums.length - 1) {
            int num = nums[i];
            if (nums[i + 1] == nums[i] + 1) {
                while (i < nums.length - 1 && nums[i + 1] == nums[i] + 1) {
                    i++;
                }
                StringBuilder sj = new StringBuilder();
                sj.append(num);
                sj.append("->");
                sj.append(nums[i]);
                out.add(sj.toString());
            } else {
                out.add(String.valueOf(num));
            }
            i++;
        }
        if (i < nums.length) {
            out.add(String.valueOf(nums[i]));
        }
        return out;
    }

    public List<String> summaryRanges2(int[] nums) {
        // 6ms
        List<String> res = new ArrayList<>();
        if (nums.length <= 0)
            return res;

        int n_start = nums[0], n_end = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1] + 1) {
                n_end = nums[i];
            } else {
                if (n_end > n_start) {
                    res.add(n_start + "->" + n_end);
                } else {
                    res.add(nums[i - 1] + "");
                }
                n_start = nums[i];
                n_end = nums[0];
            }
        }
        if (n_end > n_start) {
            res.add(n_start + "->" + n_end);
        } else {
            res.add(nums[nums.length - 1] + "");
        }

        return res;
    }

    public List<String> summaryRanges_normal(int[] nums) {
        // 8ms
        List<String> list = new ArrayList<>();

        if (nums.length == 1) {
            list.add(nums[0] + "");
            return list;
        }

        for(int i = 0; i < nums.length; i++) {
            int a = nums[i];
            while (i + 1 < nums.length && (nums[i + 1] - nums[i]) == 1) {
                i++;
            }
            if (a != nums[i]) {
                list.add(a + "->" + nums[i]);
            } else {
                list.add(a + "");
            }
        }
        return list;
    }

    public String listArrayToString(List<String> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[\"" + list.get(0) + "\"";
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += ",\"" + list.get(i) + "\"";
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringTointArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();
        
        List<String> result = summaryRanges(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

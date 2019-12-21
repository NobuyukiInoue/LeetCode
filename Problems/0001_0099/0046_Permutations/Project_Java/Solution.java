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
        
        List<List<Integer>> result = permute(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listlistIntToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public int[] distinctDifferenceArray1(int[] nums) {
        // 9ms
        int[] ans = new int[nums.length];
        HashMap<Integer, Integer> suff = new HashMap<Integer,Integer>();
        HashMap<Integer, Integer> pref = new HashMap<Integer,Integer>();
        for (int num : nums) {
            suff.put(num, suff.getOrDefault(num, 0) + 1);
        }
        for (int i = 0; i < nums.length; i++) {
            pref.put(nums[i], pref.getOrDefault(nums[i], 0) + 1);
            suff.put(nums[i], suff.get(nums[i]) - 1);
            if (suff.get(nums[i]) == 0) {
                suff.remove(nums[i]);
            }
            ans[i] = pref.size() - suff.size();
        }
        return ans;
    }

    public int[] distinctDifferenceArray2(int[] nums) {
        // 9ms - 10ms
        var diff = new int[nums.length];
        var pref = new HashMap<Integer, Integer>();
        var suff = new HashMap<Integer, Integer>();
        for (var num : nums) {
            suff.compute(num, (k, v) -> v == null ? 1 : ++v);
        }
        for (var i = 0; i < nums.length; i++) {
            pref.compute(nums[i], (k, v) -> v == null ? 1 : ++v);
            if (suff.compute(nums[i], (k, v) -> --v) == 0)
                suff.remove(nums[i]);
    
            diff[i] = pref.size() - suff.size();
        }
        return diff;
    }

    public int[] distinctDifferenceArray(int[] nums) {
        int n = nums.length;
        int suff[] =new int[51];
        int res[] = new int[n];
        for (int i : nums) {
            suff[i]++;
        }
        int pref[]=new int[51];
        for (int i = 0; i < n; i++) {
            pref[nums[i]]++;
            suff[nums[i]]--;
            int cnt_suff = 0, cnt_pref = 0;
            for (int j = 1; j <= 50; j++) {
                if (suff[j] > 0) {
                    cnt_suff++;
                }
            }
            for (int j = 1; j <= 50; j++) {
                if (pref[j] > 0) {
                    cnt_pref++;
                }
            }
            res[i] = cnt_pref - cnt_suff;
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = distinctDifferenceArray(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

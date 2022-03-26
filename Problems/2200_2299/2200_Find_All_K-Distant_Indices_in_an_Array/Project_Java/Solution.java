import java.util.*;

public class Solution {
    public List<Integer> findKDistantIndices(int[] nums, int key, int k) {
        // 3ms
        List<Integer> indices = new ArrayList<>();
        int i = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] == key) {
                if (indices.size() == 0) {
                    i = 0;
                } else {
                    i = indices.get(indices.size() - 1) + 1;
                }
                i = Math.max(j - k, i);
                int end = Math.min(j + k, nums.length - 1);
                for (; i <= end; i++) {
                    indices.add(i);
                }
            }
        }
        return indices;
    }

    public List<Integer> findKDistantIndices_normal(int[] nums, int key, int k) {
        // 9ms
        List<Integer> key_index = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == key) {
                key_index.add(i);
            }
        }
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            for (int pos = 0; pos < key_index.size(); pos++) {
                if (Math.abs(i - key_index.get(pos)) <= k) {
                    res.add(i);
                    break;
                }
            }
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int key = Integer.parseInt(flds[1]);
        int k = Integer.parseInt(flds[2]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", key = " + Integer.toString(key) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        List<Integer> result = findKDistantIndices(nums, key, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

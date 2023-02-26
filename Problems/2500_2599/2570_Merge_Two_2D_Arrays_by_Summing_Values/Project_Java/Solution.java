import java.util.*;

public class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        // 5ms
        HashMap<Integer, Integer> map = new HashMap<>();
        int i = 0, j = 0;
        while (i < nums1.length || j < nums2.length) {
            if (i == nums1.length) {
                map.put(nums2[j][0], nums2[j][1]);
                j++;
            } else if (j == nums2.length) {
                map.put(nums1[i][0], nums1[i][1]);
                i++;
            } else {
                if (nums1[i][0] == nums2[j][0]) {
                    map.put(nums1[i][0], nums1[i][1] + nums2[j][1]);
                    i++;
                    j++;
                } else if (nums1[i][0] < nums2[j][0]) {
                    map.put(nums1[i][0], nums1[i][1]);
                    i++;
                } else {
                    map.put(nums2[j][0], nums2[j][1]);
                    j++;
                }
            }
        }

        int[][] ans = new int[map.size()][2];
        int k = 0;
        for (int key : map.keySet()) {
            ans[k++] = new int[] {key, map.get(key)};
        }
        
        Arrays.sort(ans, (a, b) -> a[0] - b[0]);
        return ans;
    }

    public int[][] mergeArrays2(int[][] nums1, int[][] nums2) {
        // 5ms
        Map<Integer,Integer> map = new HashMap<>();
        for (int[] a : nums1) {
            map.put(a[0], a[1]);
        }
        for (int[] a : nums2) {
            if (map.containsKey(a[0])) {
                map.put(a[0], map.get(a[0])+a[1]);
            } else {
                map.put(a[0],a[1]);
            }
        }
        int ans[][] = new int[map.size()][2];
        int i = 0;
        for (int key : map.keySet()) {
            ans[i++] = new int[] {key,map.get(key)};
        }
        Arrays.sort(ans, (a,b) -> a[0] - b[0]);
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[[", "").replace("]]]", "").trim().split("\\]\\],\\[\\[");

        Mylib ml = new Mylib();
        int[][] nums1 = ml.stringToIntIntArray(flds[0].split("\\],\\["));
        int[][] nums2 = ml.stringToIntIntArray(flds[1].split("\\],\\["));
        System.out.println("nums1 = " + ml.intIntArrayToString(nums1) + ", nums2 = " + ml.intIntArrayToString(nums2));

        long start = System.currentTimeMillis();

        int[][] result = mergeArrays(nums1, nums2);

        long end = System.currentTimeMillis();

        System.out.println("result = [" + ml.intIntArrayToString(result) + "]");
        System.out.println((end - start)  + "ms\n");
    }
}

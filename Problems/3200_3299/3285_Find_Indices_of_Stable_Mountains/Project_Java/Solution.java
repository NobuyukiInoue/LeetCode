import java.util.*;

public class Solution {
    public List<Integer> stableMountains(int[] height, int threshold) {
        // 1ms
        List<Integer> ans = new ArrayList<>();
        for (int i = 1; i < height.length; i++) {
            if (height[i - 1] > threshold) {
                ans.add(i);
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] height = ml.stringToIntArray(flds[0]);
        int threshold = Integer.parseInt(flds[1]);
        System.out.println("height = " + ml.intArrayToString(height) + ", threshold = " + threshold);

        long start = System.currentTimeMillis();

        List<Integer> result = stableMountains(height, threshold);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

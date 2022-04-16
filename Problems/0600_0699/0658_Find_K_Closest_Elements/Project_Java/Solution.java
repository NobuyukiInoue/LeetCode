import java.util.*;
import java.util.stream.*;

public class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        // 3ms - 10ms
        int left = 0, right = arr.length - 1;
        while (right - left + 1 != k) {
            if (Math.abs(arr[left] - x) > Math.abs(arr[right] - x)) {
                left++;
            } else {
                right--;
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (int i = left; i <= right; i++) {
            ans.add(arr[i]);
        }
        return ans;
        /* 6ms - 14ms
        return Arrays.stream(arr, left, right + 1).boxed().collect(Collectors.toList());
        */
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        int x = Integer.parseInt(flds[2]);
        System.out.println("arr = " + ml.intArrayToString(arr) + ", x = " + Integer.toString(k) + ", k = " + Integer.toString(x));

        long start = System.currentTimeMillis();

        List<Integer> result = findClosestElements(arr, k, x);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

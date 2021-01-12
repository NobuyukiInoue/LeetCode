import java.util.*;

public class Solution {
    public int longestMountain(int[] arr) {
        // 2ms
        if (arr.length < 3) {
            return 0;
        }

        int largest_mountain = 0;
        int start = 0, end = 0;
        int arrLength = arr.length;
        while (end < arrLength) {
            start = end;
            if (end + 1 < arrLength && arr[end] < arr[end + 1]) {
                while (end + 1 < arrLength && arr[end] < arr[end + 1]) {
                    end++;
                }
                if (end + 1 < arrLength && arr[end] > arr[end + 1]) {
                    while (end + 1 < arrLength && arr[end] > arr[end + 1]) {
                        end++;
                    }
                    largest_mountain = Math.max(largest_mountain, end - start + 1);
                }
            }
            if (end == start) {
                end++;
            }
        }
        return largest_mountain;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr   = ml.stringToIntArray(flds);
        System.out.println("arr   = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();

        int result = longestMountain(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

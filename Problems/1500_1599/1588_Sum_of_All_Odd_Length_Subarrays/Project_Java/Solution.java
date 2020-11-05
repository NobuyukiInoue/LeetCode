import java.util.*;

public class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        // 0ms
        int sum = 0;
        for (int i = 1; i <= arr.length; i += 2) {
            sum += slidingSum(arr, i);
        }
        return sum;
    }
    
    int slidingSum(int[] arr, int windowSize){
        int res = 0;
        int sum = 0; 
        for (int i = 0; i < arr.length; i++) {
            if (i < windowSize) {
                sum += arr[i];
            } else {
                res += sum;
                sum -= arr[i - windowSize];
                sum += arr[i];
            }
        }
        return res + sum;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();
        
        int result = sumOddLengthSubarrays(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

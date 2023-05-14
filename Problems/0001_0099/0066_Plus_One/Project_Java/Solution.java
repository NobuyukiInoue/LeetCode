import java.util.*;

public class Solution {
    public int[] plusOne(int[] digits) {
        // 0ms
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        digits = new int[digits.length + 1];
        digits[0] = 1;
        return digits;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] digits = ml.stringToIntArray(flds);
        System.out.println("digits = " + ml.intArrayToString(digits));

        long start = System.currentTimeMillis();

        int[] result = plusOne(digits);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

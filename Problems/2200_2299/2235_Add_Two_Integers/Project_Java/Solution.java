import java.util.*;

public class Solution {
    public int sum(int num1, int num2) {
        // 0ms
        return num1 + num2;
    }

    public int sum_circuit(int num1, int num2) {
        // 0ms
        return add(num1, num2);
    }

    private int add(int x, int y) {
        if (y == 0) {
            return x;
        } else if (x < 0 && y < 0) {
            int s = ~x^~y;
            int c = (~x&~y)<<1;
            return ~add(add(s, c), 1);
        }
        int s = x^y;
        int c = (x&y)<<1;
        return add(s, c);
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        int num1 = nums[0], num2 = nums[1];
        System.out.println("num1 = " + Integer.toString(num1) + ", num2 = " + Integer.toString(num2));

        long t_start = System.currentTimeMillis();

        int result = sum(num1, num2);

        long t_end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((t_end - t_start)  + "ms\n");
    }
}

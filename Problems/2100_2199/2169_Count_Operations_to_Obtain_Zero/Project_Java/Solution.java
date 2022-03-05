import java.util.*;

public class Solution {
    public int countOperations(int num1, int num2) {
		// 2ms
		int res = 0;
		while (num1 != 0 && num2 != 0) {
			if (num1 >= num2) {
				num1 -= num2;
			} else {
				num2 -= num1;
			}
			res++;
		}
		return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
		int num1 = nums[0], num2 = nums[1];
        System.out.println("num1 = " + Integer.toString(num1) + ", num2 = " + Integer.toString(num2));

        long start = System.currentTimeMillis();

        int result = countOperations(num1, num2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

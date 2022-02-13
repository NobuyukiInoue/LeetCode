import java.util.*;

public class Solution {
    public int minimumSum(int num) {
        // 1ms
        int[] temp = new int[4];
        for (int i = 0; i < 4; i++) {
            temp[i] = num % 10;
            num /= 10;
        }
        Arrays.sort(temp);
        return 10*temp[0] + temp[2] + 10*temp[1] + temp[3];
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        int num = Integer.parseInt(flds);
        System.out.println("num = " + Integer.toString(num));

        long start = System.currentTimeMillis();

        int result = minimumSum(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

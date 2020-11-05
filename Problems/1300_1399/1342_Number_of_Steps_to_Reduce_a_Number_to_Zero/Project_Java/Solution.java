import java.util.*;

public class Solution {
    public int numberOfSteps (int num) {
        // 0ms
        int count = 0;
        while (num > 0) {
            if (num % 2 == 0)
                num /= 2;
            else
                num--;
            count++;
        }
        return count;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int num = Integer.parseInt(fld);
        System.out.println("num = " + Integer.toString(num));

        long start = System.currentTimeMillis();

        int result = numberOfSteps(num);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

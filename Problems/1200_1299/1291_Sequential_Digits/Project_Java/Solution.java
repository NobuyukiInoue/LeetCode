import java.util.*;

public class Solution {
    public List<Integer> sequentialDigits(int low, int high) {
        // 0ms
        List<Integer> res = new ArrayList<>();
        List<Long> total = new ArrayList<>();
        long lo = 12, fact = 11, prev = 12;

        for (int i = 9; i > 0; i--) {
            total.add(lo);
            while (lo%10 != 9) {
                lo += fact;
                total.add(lo);
            }
            fact = fact*10 + 1;
            lo = prev + fact;
            prev = lo;
        }

        for (long val:total) {
            if (val > high) {
                break;
            }
            if (val >= low && val <= high) {
                res.add((int)val);
            }
        }

        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("[[", "").replace("]]", "").replace(", ", ",").trim().split("\\],\\[");
        int low = Integer.parseInt(flds[0]);
        int high = Integer.parseInt(flds[1]);

        long start = System.currentTimeMillis();

        List<Integer> result = sequentialDigits(low, high);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

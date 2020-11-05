import java.util.*;

public class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> res = new ArrayList<>();
        for (int i = left, n = 0; i <= right; i++) {
            for (n = i; n > 0; n /= 10)
                if (n % 10 == 0 || i % (n % 10) != 0)
                    break;
            if (n == 0)
                res.add(i);
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        Integer left = Integer.parseInt(flds[0]);
        Integer right = Integer.parseInt(flds[1]);
        System.out.println("left = " + Integer.toString(left) + ", right = " + Integer.toString(right));

        long start = System.currentTimeMillis();

        List<Integer> result = selfDividingNumbers(left, right);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

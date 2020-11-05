import java.util.*;

public class Solution {

    public int numFriendRequests(int[] ages) {
        // 2ms
        if (ages == null || ages.length == 0) {
            return 0;
        }
        int[] count = new int[121];
        for (int age : ages) {
            count[age]++;
        }

        int totalRequest = 0;
        for (int i = 0; i <= 120; i++) {
            if (count[i] == 0 || (int)(0.5 * i + 8) > i) {
                continue;
            }
            totalRequest += count[i] * (count[i] - 1);
            for (int j = (int)(0.5 * i + 8); j <= i; j++) {
                if (j == i ||  count[j] == 0) {
                    continue;
                }
                totalRequest += count[j] * count[i];
            }
        }
        return totalRequest;
    }

    public int numFriendRequests2(int[] ages) {
        // 21ms
        Map<Integer, Integer> count = new HashMap<>();
        for (int age : ages)
            count.put(age, count.getOrDefault(age, 0) + 1);
        int res = 0;
        for (Integer a : count.keySet())
            for (Integer b : count.keySet())
                if (request(a, b)) res += count.get(a) * (count.get(b) - (a == b ? 1 : 0));
        return res;
    }

    private boolean request(int a, int b) {
        return !(b <= 0.5 * a + 7 || b > a || (b > 100 && a < 100));
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] ages = ml.stringToIntArray(flds);
        System.out.println("ages = " + ml.intArrayToString(ages));

        long start = System.currentTimeMillis();

        int result = numFriendRequests(ages);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

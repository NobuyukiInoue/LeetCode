import java.util.*;

public class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
        // 10ms
        Map<Integer, Integer> count = new HashMap<>();
        int res = 0;
        for (int i : deck)
            count.put(i, count.getOrDefault(i, 0) + 1);
        for (int i : count.values())
            res = gcd(i, res);
        return res > 1;
    }

    public int gcd(int a, int b) {
        return b > 0 ? gcd(b, a % b) : a;
    }
    
    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] deck = ml.stringToIntArray(flds);
        System.out.println("deck = " + ml.intArrayToString(deck));

        long start = System.currentTimeMillis();

        boolean result = hasGroupsSizeX(deck);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

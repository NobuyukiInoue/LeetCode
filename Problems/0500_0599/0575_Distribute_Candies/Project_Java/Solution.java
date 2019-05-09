import java.util.*;

public class Solution {
    public int distributeCandies(int[] candies) {
        Set<Integer> kinds = new HashSet<>();
        for (int candy : candies) kinds.add(candy);
        return kinds.size() >= candies.length / 2 ? candies.length / 2 : kinds.size();
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] candies = ml.str_to_int_array(flds);

        long start = System.currentTimeMillis();

        int result = distributeCandies(candies);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

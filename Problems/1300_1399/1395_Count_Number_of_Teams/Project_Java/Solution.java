import java.util.*;

public class Solution {
    public int numTeams(int[] rating) {
        // 13ms
        int[] arrAsc = new int[rating.length];
        int[] arrDesc = new int[rating.length];
        int ans = 0;
        for (int i = 0; i < rating.length; i++) {
            for (int j = 0; j < i; j++) {
                if (rating[i] > rating[j]) {
                    arrDesc[i]++;
                    ans += arrDesc[j];
                } else if (rating[i] < rating[j]) {
                    arrAsc[i]++;
                    ans += arrAsc[j];
                }
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] rating = ml.stringToIntArray(flds);
        System.out.println("rating = " + ml.intArrayToString(rating));

        long start = System.currentTimeMillis();

        int result = numTeams(rating);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

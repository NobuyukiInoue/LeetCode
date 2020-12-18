import java.util.*;

public class Solution {
    public int maxScore(int[] cardPoints, int k) {
        // 1ms
        int res = 0;
        int sum = 0;
        int slideSum = 0;
        int n = cardPoints.length;

        for (int i = 0; i < n; i++) {
            sum += cardPoints[i];
        }
        for (int i = 0; i < n - k; i++) {
            slideSum += (cardPoints[i]);
        }
        res = sum - slideSum;
        for (int i = n - k; i < n; i++) {
            slideSum += cardPoints[i] - cardPoints[i - (n - k)];
            res = Math.max(res, sum - slideSum);
        }
        return res;
    }
    
    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] cardPoints = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("cardPoints = " + ml.intArrayToString(cardPoints) + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = maxScore(cardPoints, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

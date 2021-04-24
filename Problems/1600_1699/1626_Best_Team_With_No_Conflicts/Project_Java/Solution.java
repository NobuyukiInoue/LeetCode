import java.util.*;

public class Solution {
    public int bestTeamScore(int[] scores, int[] ages) {
        // 24ms
        Integer[] indexes = new Integer[scores.length];

        for (int i = 0; i < indexes.length; i++) {
            indexes[i] = i;
        }

        Arrays.sort(indexes, (o1, o2) -> {
            if (scores[o1] == scores[o2]) {
                return ages[o1] - ages[o2];
            }
            return scores[o1] - scores[o2];
        });
    
        int highestAge = 0;
        for (int i : ages) {
            highestAge = Math.max(highestAge, i);
        }

        int[] BIT = new int[highestAge + 1];
        int res = Integer.MIN_VALUE;
        for (int index : indexes) {
            int currentScore = scores[index];
            int age = ages[index];
            int historicalBest = queryBIT(BIT, age);
            int currentBest = currentScore + historicalBest;
            res = Math.max(res, currentBest);
            updateBIT(BIT, age, currentBest);
        }
        return res;
    }

    private int queryBIT(int[] BIT, int age) {
        int historicalBest = Integer.MIN_VALUE;
        for (int i = age; i > 0; i -= i & (-i)) {
            historicalBest = Math.max(historicalBest, BIT[i]);
        }
        return historicalBest;
    }
    
    private void updateBIT(int[] BIT, int age, int currentBest) {
        for (int i = age; i < BIT.length; i += i & (-i)) {
            BIT[i] = Math.max(BIT[i], currentBest);
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] scores = ml.stringToIntArray(flds[0]);
        int[] ages = ml.stringToIntArray(flds[1]);
        System.out.println("scores = " + ml.intArrayToString(scores));
        System.out.println("ages = " + ml.intArrayToString(ages));

        long start = System.currentTimeMillis();

        int result = bestTeamScore(scores, ages);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

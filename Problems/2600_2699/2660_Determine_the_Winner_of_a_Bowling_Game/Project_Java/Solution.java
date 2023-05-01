import java.util.*;

public class Solution {
    public int isWinner(int[] player1, int[] player2) {
        // 2ms
        int score1 = getScore(player1);
        int score2 = getScore(player2);
        if (score1 > score2) {
            return 1;
        } else if (score1 < score2) {
            return 2;
        }
        return 0;
    }

    private int getScore(int[] nums) {
        int score = 0;
        int cnt = 0;
        for (int num : nums) {
            if (cnt > 0) {
                score += num*2;
                cnt--;
            } else {
                score += num;
            }
            if (num == 10) {
                cnt = 2;
            }
        }
        return score;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] player1 = ml.stringToIntArray(flds[0]);
        int[] player2 = ml.stringToIntArray(flds[1]);
        System.out.println("player1 = [" + ml.intArrayToString(player1) + "], player2 = [" + ml.intArrayToString(player2) + "]");
 
        long start = System.currentTimeMillis();

        int result = isWinner(player1, player2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

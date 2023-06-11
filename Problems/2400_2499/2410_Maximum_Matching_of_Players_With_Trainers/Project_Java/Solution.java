import java.util.*;

public class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        // 28ms
        Arrays.sort(players);
        Arrays.sort(trainers);
        int res = 0, i = 0, j = 0;
        while (i < players.length && j < trainers.length) {
            if (players[i] <= trainers[j]) {
                res++;
                i++;
            }
            j++;
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] players = ml.stringToIntArray(flds[0]);
        int[] trainers = ml.stringToIntArray(flds[1]);
        System.out.println("players = " + ml.intArrayToString(players) + ", trainers = " + ml.intArrayToString(trainers));

        long start = System.currentTimeMillis();

        int result = matchPlayersAndTrainers(players, trainers);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

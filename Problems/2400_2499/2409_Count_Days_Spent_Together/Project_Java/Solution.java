import java.util.*;

public class Solution {
    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        // 1ms
        int[] month = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        for (int i = 1; i < month.length; i++) {
            month[i] = month[i - 1] + month[i];
        }
        int alice_a = month[Integer.parseInt(arriveAlice.substring(0, 2)) - 1] + Integer.parseInt(arriveAlice.substring(3));
        int alice_l = month[Integer.parseInt(leaveAlice.substring(0, 2)) - 1] + Integer.parseInt(leaveAlice.substring(3));
        int bob_a = month[Integer.parseInt(arriveBob.substring(0, 2)) - 1] + Integer.parseInt(arriveBob.substring(3));
        int bob_l = month[Integer.parseInt(leaveBob.substring(0, 2)) - 1] + Integer.parseInt(leaveBob.substring(3));
        return Math.max(Math.min(alice_l, bob_l) - Math.max(alice_a, bob_a) + 1, 0);
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").split(",");
        String arriveAlice = flds[0], leaveAlice = flds[1], arriveBob = flds[2], leaveBob = flds[3];
        System.out.println("arriveAlice = " + arriveAlice + ", leaveAlice = " + leaveAlice + ", arriveBob = " + arriveBob +  ", leaveBob = " + leaveBob);

        long start = System.currentTimeMillis();

        int result = countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

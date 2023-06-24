import java.util.*;

public class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        // 7ms
        return (mainTank + Math.min((mainTank - 1)/4, additionalTank))*10;
    }

    public int distanceTraveled2(int mainTank, int additionalTank) {
        // 7ms
        int ans = 0;
        while (mainTank >= 5) {
            mainTank -= 5;
            ans += 50;
            if (additionalTank >= 1) {
                additionalTank--;
                mainTank++;
            }
        }
        return ans + mainTank*10;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int mainTank = Integer.parseInt(flds[0]);
        int additionalTank = Integer.parseInt(flds[1]);
        System.out.println("mainTank = " + mainTank + ", additionalTank = " + additionalTank);
 
        long start = System.currentTimeMillis();

        int result = distanceTraveled(mainTank, additionalTank);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

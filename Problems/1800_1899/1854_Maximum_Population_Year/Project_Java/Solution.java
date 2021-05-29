import java.util.*;

public class Solution {
    public int maximumPopulation(int[][] logs) {
        // 0ms
        int[] popChange = new int[2050 - 1950 + 1];
        for (int i = 0; i < logs.length; i++) {
            popChange[logs[i][0]-1950] += 1;
            popChange[logs[i][1]-1950] -= 1;
        }
        
        int maxPop = -1;
        int besti = -1;
        int lastiPop = 0;
        for (int i = 0; i < popChange.length; i++) {
            int currentiPop = lastiPop + popChange[i];
            if (currentiPop > maxPop) {
                maxPop = currentiPop;
                besti = 1950 + i;
            }
            lastiPop = currentiPop;
        }
        return besti;
    }

    public int maximumPopulation2(int[][] logs) {
        // 1ms
        int[] poplation = new int[2050 - 1950 + 1];
        for (int[] log : logs) {
            for (int i = log[0]; i < log[1]; i++) {
                poplation[i - 1950]++;
            }
        }

        int maxPoplation = 0;
        int maximumPoplation = 0;
        for (int i = 0; i < poplation.length; i++) {
            if (poplation[i] > maxPoplation) {
                maxPoplation = poplation[i];
                maximumPoplation = 1950 + i;
            }
        }

        return maximumPoplation;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] logs = ml.stringToIntIntArray(flds);
        System.out.println("logs = " + ml.intIntArrayToString(logs));

        long start = System.currentTimeMillis();

        int result = maximumPopulation(logs);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

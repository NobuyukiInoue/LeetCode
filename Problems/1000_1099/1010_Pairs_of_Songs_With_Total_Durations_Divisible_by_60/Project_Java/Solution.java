import java.util.*;

public class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        int[] freq = new int[60];
        for(int dur : time){
            freq[dur%60]++;
        }
        
        int res = 0;
        for (int i = 1; i <= 29; i++) {
            res += freq[i]*freq[60 - i];
        }
        res += freq[0]*(freq[0] - 1)/2;
        res += freq[30]*(freq[30] - 1)/2;

        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] time = ml.stringToIntArray(flds);
        System.out.println("time = " + ml.intArrayToString(time));

        long start = System.currentTimeMillis();

        int result = numPairsDivisibleBy60(time);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public int repeatedNTimes(int[] A) {
        int ans = 0;
        HashMap<Integer, Integer> count = new HashMap<Integer,Integer>();
        for (int i : A) {
            if(count.containsKey(i))
                return i;
            else
                count.put(i, 1);
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();

        int[] A = ml.stringTointArray(flds);

        System.out.println("A = " + ml.intArrayToString(A));

        long start = System.currentTimeMillis();
        
        int result = repeatedNTimes(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

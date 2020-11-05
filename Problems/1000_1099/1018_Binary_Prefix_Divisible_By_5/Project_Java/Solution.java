import java.util.*;

public class Solution {
    public List<Boolean> prefixesDivBy5(int[] A) {
        int total = 0;
        List<Boolean> result = new ArrayList<Boolean>();
        for (int i = 0; i < A.length; i++) {
            //total = ((total << 1) + A[i]) % 5;
            total = (total*2 + A[i]) % 5;
            if (total == 0)
                result.add(true);
            else
                result.add(false);
        }
        return result;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] A = ml.stringToIntArray(flds);
        System.out.println("A = " + ml.intArrayToString(A));

        long start = System.currentTimeMillis();

        List<Boolean> result = prefixesDivBy5(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listBooleanArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public List<Integer> findPeaks(int[] mountain) {
        // 1ms
        List<Integer> res = new ArrayList<>();
        for (int i = 1; i < mountain.length - 1; i++) {
            if (mountain[i - 1] < mountain[i] && mountain[i] > mountain[i + 1]) {
                res.add(i);
            }
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] mountain = ml.stringToIntArray(flds);
        System.out.println("mountain = " + ml.intArrayToString(mountain));

        long start = System.currentTimeMillis();

        List<Integer> result = findPeaks(mountain);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

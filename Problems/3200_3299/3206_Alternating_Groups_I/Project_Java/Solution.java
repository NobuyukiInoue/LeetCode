import java.util.*;

public class Solution {
    public int numberOfAlternatingGroups(int[] colors) {
        // 1ms
        int n = colors.length;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int j, k;
            if (i + 1 < n)
                j = i + 1;
            else
                j = i + 1 - n;
            if (colors[i] == colors[j])
                continue;
            if (i + 2 < n)
                k = i + 2;
            else
                k = i + 2 - n;
            if (colors[j] == colors[k])
                continue;
            ans++;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] colors = ml.stringToIntArray(flds);
        System.out.println("colors = " + ml.intArrayToString(colors));

        long start = System.currentTimeMillis();

        int result = numberOfAlternatingGroups(colors);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

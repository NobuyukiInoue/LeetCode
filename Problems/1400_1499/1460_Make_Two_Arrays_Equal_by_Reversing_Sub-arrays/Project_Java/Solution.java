import java.util.*;

public class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        // 2ms
        Arrays.sort(target);
        Arrays.sort(arr);
        if (Arrays.equals(target, arr))
            return true;
        return false;
    }

    public boolean canBeEqual2(int[] target, int[] arr) {
        // 1ms
        int[] cnt = new int[1001];
        for (int t : target)
            ++cnt[t];
        for (int a : arr) {
            if (--cnt[a] < 0) {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] target = mc.stringTointArray(flds[0]);
        int[] arr = mc.stringTointArray(flds[1]);

        System.out.println("target = " + mc.intArrayToString(target));
        System.out.println("arr = " + mc.intArrayToString(arr));

        long start = System.currentTimeMillis();
        
        boolean result = canBeEqual(target, arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

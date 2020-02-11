import java.util.*;

public class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int i = 0, n = bits.length - 1;
        while (i < n) {
            if (bits[i] == 1) {
                i += 2;
            } else {
                i++;
            }
        }
    
        return i == n;
    }

    public boolean isOneBitCharacter2(int[] bits) {
        int n = bits.length, i = 0;
        while (i < n - 1) {
            if (bits[i] == 0)
                i++;
            else
                i += 2;
        }
        return i == n - 1;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib mc = new Mylib();
        int[] bits = mc.stringTointArray(flds);

        System.out.println("bits = " + mc.intArrayToString(bits));

        long start = System.currentTimeMillis();
        
        boolean result = isOneBitCharacter(bits);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public int rotatedDigits(int N) {
        // 4ms
        int res = 0;
        for(int i = 0; i <= N; i++) {
            int[] tab = new int[10];
            for(char c: Integer.toString(i).toCharArray()) {
                tab[c - '0'] = 1;
            }
            if (tab[3] == 1 || tab[4] == 1 || tab[7] == 1)
                continue;
            if (tab[6] + tab[9] + tab[2] + tab[5] == 0 && tab[1] + tab[0] + tab[8] > 0)
                continue;
            res++;
        }
        return res;        
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int N = Integer.parseInt(flds);
        System.out.println("N = " + Integer.toString(N));

        long start = System.currentTimeMillis();
        
        int result = rotatedDigits(N);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

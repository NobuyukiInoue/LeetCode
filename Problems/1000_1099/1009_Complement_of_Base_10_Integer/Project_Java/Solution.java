import java.util.*;

public class Solution {
    public int bitwiseComplement(int N) {
        if (N == 0)
            return 1;
        int i = 0, temp;
        while (N > (temp = (int)Math.pow(2, i)))
            i++;
        if (N == temp)
            return N - 1;
        else
            return temp - 1 - N;        
    }
    
    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int N = Integer.parseInt(flds);
        System.out.println("N = " + Integer.toString(N));

        long start = System.currentTimeMillis();
        
        int result = bitwiseComplement(N);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

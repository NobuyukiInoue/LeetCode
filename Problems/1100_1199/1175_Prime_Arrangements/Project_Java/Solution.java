import java.util.*;

public class Solution {
    public int numPrimeArrangements(int n) {
        // 0ms
        int[] primes = new int[] {2,3,5,7,11,13,17,19,23,29,31,37,41,
            43,47,53,59,61,67,71,73,79,83,89,97};
    
        int modulo = (int)Math.pow(10,9) + 7;

        long result = 1;
        int primeCounter = 0;
        for (int i = 0; i < primes.length; ++i)
            if (primes[i] <= n)
                ++primeCounter;
            else
                break;

        for (int i = 2; i <= primeCounter; ++i)
            result = (result*i)%modulo;

        for (int i = 2; i <= n - primeCounter; ++i)
            result = (result*i)%modulo;

        return (int)result;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = numPrimeArrangements(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

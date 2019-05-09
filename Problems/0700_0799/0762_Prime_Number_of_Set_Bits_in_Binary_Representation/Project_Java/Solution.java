import java.util.stream.IntStream;
import java.util.*;

public class Solution {
    // 4ms
    public int countPrimeSetBits(int L, int R) {
        int primeCounter = 0;
        for (int i = L; i <= R; i++) {
        int noOfSetBits = Integer.bitCount(i);
        if (isPrime(noOfSetBits))
            primeCounter++;
        }
        return primeCounter;
    }

    public boolean isPrime(int no) {
        if (no == 1)
            return false;
        if (no == 2)
            return true;
        for (int i = 2; i <= Math.sqrt(no); i++) {
            if (no % i == 0)
                return false;
        }
        return true;
    }

    public int countPrimeSetBits4(int L, int R) {
        // 10ms
        //an integer has 32 bits, but arrays start at 0
        boolean[] array = new boolean[33];

        //Prime numbers
        array[2] = true;
        array[3] = true; 
        array[5] = true;
        array[7] = true;
        array[11] = true;
        array[13] = true;
        array[17] = true;
        array[19] = true;
        array[23] = true;
        array[29] = true;
        array[31] = true;
        
        int toReturn = 0;
        for (int i = L; i <= R; i++) {
            //counts of bits set to 1
            int bitsSet = 0;
            int temp = i;
            while (temp != 0) {
                if(temp % 2 == 1){ //check if last bit of temp is 1
                    bitsSet++;
                }
                temp = temp >>> 1;
            }
            if (array[bitsSet]) { //if the number of set bits is prime
                toReturn++;
            }
        }
        return toReturn;
    }

    public int countPrimeSetBits2(int L, int R) {
        // 18ms
        Set<Integer> primes = new HashSet<>(Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19 /*, 23, 29 */ ));
        int cnt = 0;
        for (int i = L; i <= R; i++) {
            int bits = 0;
            for (int n = i; n > 0; n >>= 1)
                bits += n & 1;
            cnt += primes.contains(bits) ? 1 : 0;
        }
        return cnt;        
    }

    public int countPrimeSetBits3(int L, int R) {
        // 53ms
        Set<Integer> primes = new HashSet<>(Arrays.asList(2, 3, 5, 7, 11, 13, 17, 19));
        return (int)IntStream.range(L, R + 1).map(Integer::bitCount).filter(primes::contains).count();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int L = Integer.parseInt(flds[0]);
        int R = Integer.parseInt(flds[1]);
        System.out.println("L = " + Integer.toString(L) + ", R = " + Integer.toString(R));

        long start = System.currentTimeMillis();
        
        int result = countPrimeSetBits(L, R);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

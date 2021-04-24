import java.util.*;

public class Solution {
    public int numFactoredBinaryTrees(int[] arr) {
        // 10ms
        Arrays.sort(arr);
        Map<Long, Integer> numbers = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            numbers.put((long) arr[i], i);
        }
    
        long[] memo = new long[arr.length];
        Arrays.fill(memo, 1);
        long count = 0;
        for (int idx = 0; idx < arr.length; idx++) {
            for (int i = 0; i <= idx; i++) {
                long mul = ((long) arr[i])*arr[idx];
                if(mul > Integer.MAX_VALUE) {
                     break;
                }
                Integer pos = numbers.get(mul);
                if (pos != null) {
                    int factor = arr[i] == arr[idx] ? 1 : 2;
                    memo[pos] += factor * memo[i] * memo[idx];
                }
            }
            count += memo[idx];
        }
        return (int)(count % 1000000007);
    }

    public int numFactoredBinaryTrees2(int[] arr) {
        // 33ms
        long res = 0L, mod = (long)1e9 + 7;
        Arrays.sort(arr);
        HashMap<Integer, Long> dp = new HashMap<>();
        for (int i = 0; i < arr.length; ++i) {
            dp.put(arr[i], 1L);
            for (int j = 0; j < i; ++j) {
                if (arr[i] % arr[j] == 0) {
                    dp.put(arr[i], (dp.get(arr[i]) + dp.get(arr[j]) * dp.getOrDefault(arr[i] / arr[j], 0L)) % mod);
                }
            }
            res = (res + dp.get(arr[i])) % mod;
        }
        return (int)res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();

        int result = numFactoredBinaryTrees(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

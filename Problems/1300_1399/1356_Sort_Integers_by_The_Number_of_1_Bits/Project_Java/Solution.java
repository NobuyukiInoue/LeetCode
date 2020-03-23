import java.util.*;

public class Solution {
    public int[] sortByBits1(int[] arr) {
        // 11ms
        return Arrays.stream(arr).boxed().sorted(Comparator.comparingInt(i -> Integer.bitCount(i) * 10000 + i)).mapToInt(i -> i).toArray();
    }

    public int[] sortByBits(int[] arr) {
        // 6ms
        Arrays.sort(arr);
        int maxBits = 0;
        int temp = arr[arr.length - 1];
        while (temp > 0) {
            temp >>= 1;
            maxBits++;
        }

        List<Integer>[] table = (List<Integer>[]) new List[maxBits];
        for (int i = 0; i < table.length; i++) {
            table[i] = new ArrayList<>();
        }

        for (int i = 0; i < arr.length; i++) {
            int bits = bitCount(arr[i]);
            table[bits].add(arr[i]);
        }

        int[] res = new int[arr.length];
        int index = 0;
        for (int i = 0; i < table.length; i++) {
            for (int j = 0; j < table[i].size(); j++) {
                res[index++] = table[i].get(j);
            }
        }

        return res;
    }

    private int bitCount(int num) {
        int count = 0;
        while (num > 0) {
            if (num % 2 == 1)
                count++;
            num >>= 1;
        }
        return count;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringTointArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();
        
        int[] result = sortByBits(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

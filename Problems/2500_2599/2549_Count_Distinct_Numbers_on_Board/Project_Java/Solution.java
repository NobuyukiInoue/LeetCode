import java.util.*;

public class Solution {
    public int distinctIntegers(int n) {
        // 0ms
        return (n - 1) > 1 ? n - 1 : 1;
    }

    public int distinctIntegers_HashSet(int n) {
        // 188m
        Set<Integer> board = new HashSet<>();
        board.add(n);
        int size = board.size();
        while (true) {
            for (int i = 1; i < n; i++) {
                for (int x : new ArrayList<>(board)) {
                    if (x % i == 1) {
                        board.add(i);
                    }
                }
            }
            if (size == board.size()) {
                break;
            }
            size = board.size();
        }
        return size;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = distinctIntegers(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

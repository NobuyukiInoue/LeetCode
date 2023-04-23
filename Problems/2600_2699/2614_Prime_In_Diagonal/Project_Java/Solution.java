import java.util.*;

public class Solution {
    public int diagonalPrime(int[][] nums) {
        // 3ms
        ArrayList<Integer> diagonals = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (i != -(i + 1)) {
                diagonals.add(nums[i][i]);
                diagonals.add(nums[i][nums.length - (i + 1)]);
            } else {
                diagonals.add(nums[i][i]);
            }
        }
        Collections.sort(diagonals);
        for (int i = diagonals.size() - 1; i >= 0; i--) {
            if (isPrime(diagonals.get(i))) {
                return diagonals.get(i);
            }
        }
        return 0;
    }

    private boolean isPrime(int n) {
        if (n == 1)
            return false;
        if (n == 2 || n == 3)
            return true;
        if (n % 2 == 0 || n % 3 == 0)
            return false;
        int limit = (int)Math.sqrt(n);
        for (int i = 5; limit - i >= 0; i+= 2) {
            if (n % i == 0)
                return false;
        }
        return true;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] nums = ml.stringToIntIntArray(str_mat);
        System.out.println("nums = " + ml.matrixToString(nums));

        long start = System.currentTimeMillis();

        int result = diagonalPrime(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

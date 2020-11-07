import java.util.*;

public class Solution {
    public int sumSubarrayMins(int[] A) {
        // 26ms
        int res = 0, n = A.length, mod = (int)1e9 + 7;
        int[] left = new int[n], right = new int[n];
        Stack<int[]> s1 = new Stack<>(), s2 = new Stack<>();
        for (int i = 0; i < n; ++i) {
            int count = 1;
            while (!s1.isEmpty() && s1.peek()[0] > A[i])
                count += s1.pop()[1];
            s1.push(new int[] {A[i], count});
            left[i] = count;
        }
        for (int i = n - 1; i >= 0; --i) {
            int count = 1;
            while (!s2.isEmpty() && s2.peek()[0] >= A[i])
                count += s2.pop()[1];
            s2.push(new int[] {A[i], count});
            right[i] = count;
        }
        for (int i = 0; i < n; ++i)
            res = (res + A[i] * left[i] * right[i]) % mod;
        return res;
    }

    public int sumSubarrayMins2(int[] A) {
        // Time Limit Exceeded.
        return dp(A, A.length - 1);
    }

    private int dp(int[] A, int index) {
        int MOD = 1000000007;
        
        if (0 == index) {
            return A[0];
        }
        
        int sum = dp(A, index - 1);
        int min = A[index];
        
        for (int i = index; i >= 0; i--) {
            if (A[i] < min) {
                min = A[i];
            }
            sum += min;
        }
        
        return sum % MOD;
    }

    public int sumSubarrayMins3(int[] A) {
        // bad.
        int MOD = 1000000007;
        int[] pre = new int[A.length];
        int[] helper = new int[A.length + 1];
        for (int i = 0; i < A.length; i++) {
            int j = i - 1;
            while (j >= 0 && A[j] > A[i])
                j = pre[j];
            pre[i] = j;
            if (j == -1)
                helper[i] = helper[A.length - 1] + (i - j)*A[i];
            else
                helper[i] = helper[j] + (i - j)*A[i];
        }
        return arraySum(helper)%MOD;
    }

    private int arraySum(int[] nums) {
        if (nums.length == 0)
            return 0;
        int total = nums[0];
        for (int i = 1; i < nums.length; i++)
            total += nums[i];
        return total;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] A = ml.stringToIntArray(flds);
        System.out.println("A = " + ml.intArrayToString(A));

        long start = System.currentTimeMillis();

        int result = sumSubarrayMins(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

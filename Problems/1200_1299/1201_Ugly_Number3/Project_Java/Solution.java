import java.util.*;

public class Solution {
    public int nthUglyNumber(int n, int a, int b, int c) {
        // 0ms
        long ans = 0;
        long[] arr = new long[]{a, b, c};
        for (long k : arr) {
            ans = binarySearch(n, k, arr);
            if (ans > 0) {
                break;
            }
        }
        return (int) ans;
    }

    private long gcd(long n, long m) {
        if (m == 0) {
            return n;
        }
        return gcd(m, n % m);
    }

    private long binarySearch(int n, long k, long[] arr) {
        int left = 1, right = n;
        long a = arr[0] * arr[1] / gcd(arr[0], arr[1]), b = arr[0] * arr[2] /  gcd(arr[0], arr[2]), c = arr[1] * arr[2] /  gcd(arr[1], arr[2]);
        long d = a * arr[2] / gcd(a, arr[2]);
        while (left <= right) {
            int mid = (left + right) / 2;
            long val = mid * k;
            long m = val / arr[0] + val / arr[1] + val / arr[2]
                    - val / a - val / b - val / c
                    + val / d;
            if (m == n) {
                return val;
            } else if (m < n) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        int n = Integer.parseInt(flds[0]);
        int a = Integer.parseInt(flds[1]);
        int b = Integer.parseInt(flds[2]);
        int c = Integer.parseInt(flds[3]);
        System.out.println("n = " + Integer.toString(n) + ", a = " + Integer.toString(a) + ", b = " + Integer.toString(b) + ", c = " + Integer.toString(c));

        long start = System.currentTimeMillis();

        int result = nthUglyNumber(n, a, b, c);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

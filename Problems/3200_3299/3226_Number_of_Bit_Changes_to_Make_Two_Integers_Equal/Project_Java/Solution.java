import java.util.*;

public class Solution {
    public int minChanges(int n, int k) {
        // 0ms - 1ms
        int ans = 0;
        while (n > 0 || k > 0) {
            int m_n = n%2;
            int m_k = k%2;
            if (m_n == 1 && m_k == 0) {
                ans++;
            }
            if (m_n == 0 && m_k == 1) {
                return -1;
            }
            n /= 2;
            k /= 2;
        }
        return ans;
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int n = Integer.parseInt(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("n = " + n + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = minChanges(n, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

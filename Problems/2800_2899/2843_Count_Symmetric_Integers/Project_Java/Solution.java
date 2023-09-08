import java.util.*;

public class Solution {
    public int countSymmetricIntegers(int low, int high) {
        // 26ms
        int ans = 0;
        for (int num = low; num <= high; ++num) {
            String s_num = Integer.toString(num);
            int total = 0, n = s_num.length();
            for (int i = 0; i < n / 2; ++i) {
                total += s_num.charAt(i) - s_num.charAt(n - i - 1);
            }
            if (n % 2 == 0 && total == 0) {
                ans++;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int low = Integer.parseInt(flds[0]);
        int high = Integer.parseInt(flds[1]);
        System.out.println("low = " + low + ", high = " + high);
 
        long start = System.currentTimeMillis();

        int result = countSymmetricIntegers(low, high);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

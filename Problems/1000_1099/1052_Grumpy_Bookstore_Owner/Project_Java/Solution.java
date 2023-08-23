import java.util.*;

public class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        // 2ms
        int total = 0;
        int n = customers.length;
        for (int i = 0; i < n; i++) {
            total += customers[i] * (1 - grumpy[i]);
            grumpy[i] = customers[i] * grumpy[i];
        }
        int m_customers = 0;
        for (int i = 0; i < minutes; i++) {
            m_customers += grumpy[i];
        }
        int save = m_customers;
        for (int i = minutes; i < n; i++) {
            save += grumpy[i] - grumpy[i - minutes];
            if (save > m_customers) {
                m_customers = save;
            }
        }
        return total + m_customers;
    }

    public int maxSatisfied2(int[] customers, int[] grumpy, int minutes) {
        // 4ms
        int m_custmers = 0, ans = 0, tmp = 0;
        for (int i = 0; i < customers.length; i++) {
            if (grumpy[i] == 0) {
                ans += customers[i];
                customers[i] = 0;
            } else {
                tmp += customers[i];
            }
            if (i >= minutes) {
                tmp -= customers[i - minutes];
            }
            m_custmers = Math.max(m_custmers, tmp);
        }
        return ans + m_custmers;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] customers = ml.stringToIntArray(flds[0]);
        int[] grumpy = ml.stringToIntArray(flds[1]);
        int minutes = Integer.parseInt(flds[2]);
        System.out.println("customers = " + ml.intArrayToString(customers) + ", grumpy = " + ml.intArrayToString(grumpy) + ", minutes = " + minutes);
 
        long start = System.currentTimeMillis();

        int result = maxSatisfied(customers, grumpy, minutes);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public String getPermutation(int n, int k) {
        // 1ms
        if (n == 0)
            return "";

        int[] mark = new int[n];
        StringBuilder sb = new StringBuilder();
        mark[0] = 1;
        for (int i = 1; i < n; i++)
            mark[i] = (i + 1)*mark[i - 1];

        boolean[] used = new boolean[n];
        int len = n;

        for (int i = 0 ; i < n; i++) {
            int num = (k - 1)/(mark[n - 1 - i]/len) + 1;
            k = (k - 1)%(mark[n - 1 - i]/len) + 1;
            len--;
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (used[j])
                    continue;
                count++;
                if (count == num) {
                    sb.append(j + 1);
                    used[j] = true;
                    break;
                }
            }            
        }
        return sb.toString();
    }

    public String intArrayToString(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";
            result += Integer.toString(data[i]);
        }
    
        return result;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");
        int n = Integer.parseInt(flds[0]);
        int k = Integer.parseInt(flds[1]);

        long start = System.currentTimeMillis();
        
        String result = getPermutation(n, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

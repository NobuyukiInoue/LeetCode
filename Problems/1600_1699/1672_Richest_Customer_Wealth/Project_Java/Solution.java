import java.util.*;

public class Solution {
    public int maximumWealth(int[][] accounts) {
        // 0ms
        int ans = 0;
        for (int i = 0; i < accounts.length; i++) {
            int temp = arraySum(accounts[i]);
            if (temp > ans)
                ans = temp;
        }
        return ans;
    }

    private int arraySum(int[] data) {
        if (data == null)
            return 0;
        if (data.length <= 0)
            return 0;

        int total = data[0];
        for (int i = 1; i < data.length; i++)
            total += data[i];

        return total;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] accounts = new int[flds.length][];
        for (int i = 0; i < accounts.length; i++)
            accounts[i] = ml.stringToIntArray(flds[i]);
        System.out.println("accounts = " + ml.intIntArrayToString(accounts));

        long start = System.currentTimeMillis();

        int result = maximumWealth(accounts);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public int leastInterval(char[] tasks, int n) {
        // 2ms
        if (tasks == null || tasks.length == 0) {
            return 0;
        }

        int[] cnt = new int[26];
        for (char c: tasks) {
            cnt[c - 'A']++;
        }
        Arrays.sort(cnt);

        int max = cnt[25]-1;
        int spaces = max * n;
        for (int i = 24; i >= 0; i--) {
            spaces -= Math.min(max, cnt[i]);
        }
        spaces = Math.max(0, spaces);
        return tasks.length + spaces;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        char[] tasks = flds[0].replace(",", "").toCharArray();
        int n = Integer.parseInt(flds[1]);
        System.out.println("tasks = " + new String(tasks) + ", n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = leastInterval(tasks, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

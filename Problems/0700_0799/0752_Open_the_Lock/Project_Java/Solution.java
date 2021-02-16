import java.util.*;

public class Solution {
    public int openLock(String[] deadends, String target) {
        // 10ms
        boolean[] dead = new boolean[10000];

        for (String d : deadends)
            dead[Integer.parseInt(d)] = true;

        if (dead[0])
            return -1;

        dead[0] = true;

        int t = Integer.parseInt(target), ans = 0;
        LinkedList<Integer> list = new LinkedList<>();
        list.add(0);

        while (list.size() > 0) {
            int n = list.size();
            for (int i = 0; i < n; i++) {
                int cur = list.pollFirst();
                if (cur == t)
                    return ans;
                for (int m = 1; m <= 1000; m *= 10) {
                    int x = (cur % (m*10)) / m;
                    int y = x == 9 ? cur - (m*9) : cur + m;
                    if (!dead[y]) {
                        list.offerLast(y);
                        dead[y] = true;
                    }
                    y = x == 0 ? cur + (m*9) : cur - m;
                    if (!dead[y]) {
                        list.offerLast(y);
                        dead[y] = true;
                    }
                }
            }
            ans++;
        }
        return -1;
    }

    public int openLock2(String[] deadends, String target) {
        // 71ms
        Set<String> visited = new HashSet<>();
        Set<String> deadSet = new HashSet<>(Arrays.asList(deadends));
        Queue<String> queue = new LinkedList<>();
        int level = 0;

        queue.offer("0000");

        while (!queue.isEmpty()) {
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                String s = queue.poll();

                if (visited.contains(s))
                    continue;
                if (deadSet.contains(s))
                    continue;
                if (s.equals(target))
                    return level;

                visited.add(s);

                char[] cArr = s.toCharArray();

                for (int j = 0; j < cArr.length; j++) {
                    char tmp = cArr[j];

                    if (cArr[j] < '9')
                        cArr[j]++;
                    else
                        cArr[j] = '0';
                    queue.offer(new String(cArr));
                    cArr[j] = tmp;

                    if (cArr[j] > '0')
                        cArr[j]--;
                    else
                        cArr[j] = '9';
                    queue.offer(new String(cArr));
                    cArr[j] = tmp;
                }
            }
            level++;
        }

        return -1;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        String[] deadends = ml.stringToStringArray(flds[0]);
        String target = flds[1];

        System.out.println("deadends  = " + ml.stringArrayToString(deadends));
        System.out.println("target = " + target);

        long start = System.currentTimeMillis();

        int result = openLock(deadends, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

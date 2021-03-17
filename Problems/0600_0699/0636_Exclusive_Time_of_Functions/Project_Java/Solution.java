import java.util.*;

public class Solution {
    public int[] exclusiveTime(int n, List<String> logs) {
        // 10ms
        int[] res = new int[n];
        Stack<int[]> stack = new Stack<>();

        for (String log : logs) {
            String[] flds = log.split(":");
            int ID = Integer.parseInt(flds[0]);
            String op = flds[1];
            int time = Integer.parseInt(flds[2]);
            if (op.equals("start")) {
                if (stack.size() > 0) {
                    res[stack.get(stack.size() - 1)[0]] += time - stack.get(stack.size() - 1)[1];
                }
                stack.add(new int[] {ID, time});
            } else {
                int[] prev = stack.pop();
                res[ID] += time - prev[1] + 1;
                if (stack.size() > 0) {
                    stack.get(stack.size() - 1)[1] = time + 1;
                }
            }
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int n = Integer.parseInt(flds[0]);
        List<String> logs = ml.stringArrayToListStringArray(flds[1].split(","));
        System.out.println("n = " + Integer.toString(n));
        System.out.println("logs = " + ml.listStringArrayToString(logs));

        long start = System.currentTimeMillis();

        int[] result = exclusiveTime(n, logs);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

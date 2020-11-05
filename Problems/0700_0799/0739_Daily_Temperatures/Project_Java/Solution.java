public class Solution {

    public int[] dailyTemperatures(int[] T) {
        // 3ms
        int[] stack = new int[T.length];
        int top = -1;
        int[] ret = new int[T.length];
        for (int i = 0; i < T.length; i++) {
            while (top > -1 && T[i] > T[stack[top]]) {
                int idx = stack[top--];
                ret[idx] = i - idx;
            }
            stack[++top] = i;
        }
        return ret;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] T = ml.stringToIntArray(flds);

        System.out.println("T = " + ml.intArrayToString(T));

        long start = System.currentTimeMillis();

        int[] result = dailyTemperatures(T);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

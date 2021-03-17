import java.util.*;

public class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        // 1ms
        Stack<Integer> stack = new Stack<>();
        int i = 0;
        for (int x : pushed) {
            stack.push(x);
            while (stack.size() > 0 && stack.peek() == popped[i]) {
                i++;
                stack.pop();
            }
        }
        return stack.size() == 0;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] pushed = ml.stringToIntArray(flds[0]);
        int[] popped = ml.stringToIntArray(flds[1]);
        System.out.println("pushed = " + ml.intArrayToString(pushed));
        System.out.println("popped = " + ml.intArrayToString(popped));

        long start = System.currentTimeMillis();

        boolean result = validateStackSequences(pushed, popped);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public int mctFromLeafValues(int[] arr) {
        // 1ms
        Stack<Integer> stack = new Stack<>();
        int result = 0;
        for (int i = 0; i < arr.length; i++) {
            while(!stack.empty() && stack.peek() <= arr[i]) {
                /*
                int temp = stack.pop();
                if (stack.empty()) {
                    result += temp*arr[i];
                } else {
                    result += temp*Math.min(stack.peek(), arr[i]);
                }
                */
                result += stack.pop() * (stack.empty() ? arr[i] : Math.min(stack.peek(), arr[i]));
            }
            stack.push(arr[i]);
        }
        while (stack.size() > 1) {
            result += stack.pop() * stack.peek();
        }
        return result;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();

        int result = mctFromLeafValues(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        // 4ms
        Stack<Integer> stack = new Stack<>();
        for (int asteroid : asteroids) {
            if (asteroid < 0) {
                while (asteroid < 0 && !stack.isEmpty() && stack.peek() > 0) {
                    if (stack.peek() > Math.abs(asteroid)) {
                        asteroid = 0;
                    } else if (stack.peek() == Math.abs(asteroid)) {
                        stack.pop();
                        asteroid = 0;
                    } else {
                        stack.pop();
                    }
                }
                if (asteroid != 0) {
                    stack.push(asteroid);
                }
            } else {
                stack.push(asteroid);
            }
        }

        return stackToIntArray(stack);
    }

    private int[] stackToIntArray(Stack<Integer> stack) {
        int[] res = new int[stack.size()];
        for (int i = stack.size() - 1; i >= 0; i--) {
            res[i] = stack.pop();
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] asteroids = ml.stringToIntArray(flds);
        System.out.println("arr = " + ml.intArrayToString(asteroids));

        long start = System.currentTimeMillis();
        
        int[] result = asteroidCollision(asteroids);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

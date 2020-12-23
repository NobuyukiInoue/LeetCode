import java.util.*;

public class Solution {
    public int numSteps(String s) {
        // 0ms
        int res = 0, carry = 0;
        for (int i = s.length() - 1; i > 0; i--) {
            res++;
            if (s.charAt(i) - '0' + carry == 1) {
                carry = 1;
                res++;
            }
        }
        return res + carry;
    }

    public int numSteps2(String s) {
        // 0ms
        char[] char_s = s.toCharArray();
        int index = char_s.length - 1;
        boolean carry = false;
        int steps = 0;
        int prev_index_with_one = char_s.length - 1;
        while (index > 0) {
            if (carry) {
                if (char_s[index] == '0') {
                    steps += prev_index_with_one - index;
                    char_s[index] = '1';
                    index++;
                    carry = false;
                }
            } else {
                if (char_s[index] == '0') {
                    steps++;
                } else {
                    prev_index_with_one = index;
                    steps++;
                    carry = true;
                }
            }
            index--;
        }
        if (carry)
            steps += prev_index_with_one + 1;
        return steps;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = numSteps(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

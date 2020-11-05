import java.util.*;

public class Solution {
    public List<Integer> diffWaysToCompute(String input) {
        // 2ms
        List<Integer> res = new ArrayList<Integer>();

        if (isNumeric(input)) {
            res.add(Integer.parseInt(input));
            return res;
        }

        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);
            if (ch == '+' || ch == '-' || ch == '*') {
                List<Integer> res_l = diffWaysToCompute(input.substring(0, i));
                List<Integer> res_r = diffWaysToCompute(input.substring(i + 1));
                for (int leftNum : res_l) {
                    for (int rightNum : res_r) {
                        res.add(calc(leftNum, rightNum, ch));
                    }
                }
            }
        }
        return res;
    }

    private Boolean isNumeric(String data) {
        for (int i = 0; i < data.length(); i++) {
            if (!Character.isDigit(data.charAt(i))) {
                return false;
            }
        }
        return true;
    }

    private int calc(int m, int n, char ope) {
        if (ope == '+')
            return m + n;
        else if (ope == '-')
            return m - n;
        return m * n;
    }

    public void Main(String temp) {
        String input = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("path = " + input);

        long start = System.currentTimeMillis();

        List<Integer> result = diffWaysToCompute(input);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

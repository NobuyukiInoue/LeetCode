import java.util.*;

public class Solution {
    public String solveEquation(String equation) {
        // 1ms
        String flds[] = equation.split("=");
        int[] kb1 = helper(flds[0]);
        int[] kb2 = helper(flds[1]);
        int x = kb1[0] - kb2[0];
        int n = kb2[1] - kb1[1];
        if (x == 0) {
            if (n == 0) {
                return "Infinite solutions";
            }
            return "No solution";
        }
        return "x=" + Integer.toString(n / x);
    }

    private int[] helper(String s) {
        int sign = 1, n = s.length();
        int[] kb = new int[]{0, 0};
        int i = 0;
        while (i < n) {
            if (s.charAt(i) == '+') {
                sign = 1;
            } else if (s.charAt(i) == '-') {
                sign = -1;
            } else if (isDigit(s.charAt(i))) {
                int j = i;
                while (j < n && isDigit(s.charAt(j))) {
                    j++;
                }
                int tmp = Integer.parseInt(s.substring(i, j));
                if (j < n && s.charAt(j) == 'x') {
                    kb[0] += tmp * sign;
                    j++;
                } else {
                    kb[1] += tmp * sign;
                }
                i = j - 1;
            } else {
                kb[0] += 1 * sign;
            }
            i++;
        }
        return kb;
    }

    private boolean isDigit(char ch) {
        if ('0' <= ch && ch <= '9') {
            return true;
        }
        return false;
    }

    public String solveEquation2(String equation) {
        // 7ms
        int[] res = evaluateExpression(equation.split("=")[0]),  
              res2 = evaluateExpression(equation.split("=")[1]);
        res[0] -= res2[0];
        res[1] = res2[1] - res[1];
        if (res[0] == 0 && res[1] == 0) {
            return "Infinite solutions";
        }
        if (res[0] == 0) {
            return "No solution";
        }
        return "x=" + res[1]/res[0];
    }  

    public int[] evaluateExpression(String exp) {
        String[] tokens = exp.split("(?=[-+])"); 
        int[] res =  new int[2];
        for (String token : tokens) {
            if (token.equals("+x") || token.equals("x")) {
                res[0] += 1;
            } else if (token.equals("-x")) {
                res[0] -= 1;
            } else if (token.contains("x")) {
                res[0] += Integer.parseInt(token.substring(0, token.indexOf("x")));
            } else {
                res[1] += Integer.parseInt(token);
            }
        }
        return res;
    }

    public void Main(String temp) {
        String equation = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("equation = " + equation);

        long start = System.currentTimeMillis();

        String result = solveEquation(equation);

        long end = System.currentTimeMillis();

        System.out.println("result = " + "\"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}

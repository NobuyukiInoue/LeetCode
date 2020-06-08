import java.util.*;

public class Solution {
    public int calculate(String s) {
        // 4ms
        char op = '+', op2 = '+';
        int prefix = 0, count = 0, val = 0;
        boolean expr1 = false;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                count = count * 10 + c - '0';
            }
            else if (c == ' ')
                continue;
            else {
                if (c == '/' || c == '*') {
                    if (op == '/')
                        count = val / count;
                    else if (op == '*')
                        count = val * count;
                    val = count;
                    expr1 = true;
                }
                else {
                    if (op == '+')
                        prefix += count;
                    else if (op == '-') 
                        prefix -= count;
                    else if (op == '/')
                        prefix += op2 == '+' ? val/count : -val/count;
                    else if (op == '*')
                        prefix += op2 == '+' ? val*count : -val*count;
                    val = 0;
                    op2 = c;
                    expr1 = false;
                }
                count = 0;                
                op = c;
            }
        }
        if (expr1)
			count = op == '*' ? val * count : op == '/' ? val / count : 0;
        if (count > 0)
			prefix += op2 == '+' ? count : -count;
        return prefix;
    }

    public int calculate2(String s) {
        // 9ms
        int preNum = 0, preSign = 1, result = 0, i = 0, n = s.length();
        boolean toMultiply = false, toDivide = false;
        while (i < n) {
            switch (s.charAt(i)) {
                case ' ':
                    break;
                case '+':
                    result += preNum * preSign;
                    preNum = 0;
                    preSign = 1;
                    break;
                case '-':
                    result += preNum * preSign;
                    preNum = 0;
                    preSign = -1;
                    break;
                case '*':
                    toMultiply = true;
                    break;
                case '/':
                    toDivide = true;
                    break;
                default:
                    int curNum = s.charAt(i) - '0';
                    while (i < n - 1 && Character.isDigit(s.charAt(i + 1))) {
                        curNum = curNum * 10 + s.charAt(i + 1) - '0';
                        i++;
                    }
                    if (toMultiply) {
                        preNum *= curNum;
                        toMultiply = false;
                    } else if (toDivide) {
                        preNum /= curNum;
                        toDivide = false;
                    } else {
                        preNum = curNum;
                    }
            }
            i++;
        }
        return result += preNum * preSign;
    }
    
    public int calculate_stack(String s) {
        // 12ms
        int num = 0;
        char presign = '+';
        Stack<Integer> stack = new Stack<>();
        s += "+";
        for (char ch : s.toCharArray()) {
            if (Character.isDigit(ch)) {
                num = num*10 + Integer.parseInt(Character.toString(ch));
            } else if (ch == '+' || ch == '-' || ch == '*' || ch == '/') {
                if (presign == '+') {
                    stack.add(num);
                }
                else if (presign == '-') {
                    stack.add(-num);
                }
                else if (presign == '*') {
                    stack.add(stack.pop()*num);
                }
                else if (presign == '/') {
                    stack.add(stack.pop()/num);
                }
                presign = ch;
                num = 0;
            }
        }

        int total = stack.get(0);
        for (int i = 1; i < stack.size(); i++)
            total += stack.get(i);

        return total;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();
        
        int result = calculate(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

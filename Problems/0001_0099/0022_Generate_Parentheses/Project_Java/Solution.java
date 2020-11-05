import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> list = new ArrayList<String>();
        char[] str = new char[n*2];

        helper(n, n, str, 0, list);

        return list;
    }
    
    public void helper(int left, int right, char[] str, int i, List<String> list) {
        if (left < 0 || right < left) {
            return;
        }

        if (left == 0 && right == 0) {
            list.add(String.copyValueOf(str));
        }
        else {
            str[i] = '(';
            helper(left - 1, right, str, i + 1, list);
            str[i] = ')';
            helper(left, right - 1, str, i + 1, list);
        }
    }

    public void Main(String temp) {
        int n = Integer.parseInt(temp);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();
        
        List<String> result = generateParenthesis(n);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println("Execute time ... " + Long.toString(end - start)  + "ms\n");
    }
}

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

    private String list_to_String(List<String> list)
    {
        String outputStr = "";
        int listSize = list.size();
        for (int i = 0; i < listSize; ++i)
        {
            outputStr += Integer.toString(i + 1) + ":" + list.get(i) + "\n";
        }

        return outputStr;
    }

    private void list_to_Console(List<String> list)
    {
        int listSize = list.size();
        for (int i = 0; i < listSize; ++i)
        {
            System.out.println(Integer.toString(i + 1) + ":" + list.get(i));
        }
    }

    public void Main(String temp) {
        int n = Integer.parseInt(temp);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();
        
        List<String> result = generateParenthesis(n);

        long end = System.currentTimeMillis();

        System.out.println("count = " + result.size());
        System.out.println("Execute time ... " + Long.toString(end - start)  + "ms\n");

        /*
        start = System.currentTimeMillis();
        System.out.println("result = \n" + list_to_String(result));
        end = System.currentTimeMillis();
        System.out.println("List<String> to String Execute time ... " + Long.toString(end - start)  + "ms\n");
        */

        start = System.currentTimeMillis();
        list_to_Console(result);
        end = System.currentTimeMillis();
        System.out.println("List<String> to Console Execute time ... " + Long.toString(end - start)  + "ms\n");
    }
}

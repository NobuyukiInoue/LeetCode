import java.util.*;

public class Solution {
    public List<String> addOperators(String num, int target) {
        // 7ms
        List<String> res = new LinkedList<>();
        if (num.length() == 0)
            return res;

        char[] path = new char[num.length()*2 - 1];
        char[] digits = num.toCharArray();
        long n = 0;
        for (int i = 0; i < digits.length; i++) {
            n = n*10 + digits[i] - '0';
            path[i] = digits[i];
            dfs(res, path, i + 1, 0, n, digits, i + 1, target);
            if (n == 0)
                break;
        }

        return res;
    }

    private void dfs(List<String> res, char[] path, int len, long left, long cur, char[] digits, int pos, int target) {
        if (pos == digits.length) {
            if (left + cur == target)
                res.add(new String(path, 0, len));
            return;
        }

        long n = 0;
        int j = len + 1;
        for (int i = pos; i < digits.length; i++) {
            n = n*10 + digits[i] - '0';
            path[j++] = digits[i];

            path[len] = '+';
            dfs(res, path, j, left + cur, n, digits, i + 1, target);

            path[len] = '-';
            dfs(res, path, j, left + cur, -n, digits, i + 1, target);

            path[len] = '*';
            dfs(res, path, j, left, cur * n, digits, i + 1, target);

            if (digits[pos] == '0')
                break; 
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");
        String num = flds[0];
        int target = Integer.parseInt(flds[1]);

        long start = System.currentTimeMillis();

        List<String> result = addOperators(num, target);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

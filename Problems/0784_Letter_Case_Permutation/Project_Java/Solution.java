import java.util.*;

public class Solution {
    public List<String> letterCasePermutation(String S) {
        if (S == null) {
            return new LinkedList<>();
        }
        
        List<String> res = new LinkedList<>();
        helper(S.toCharArray(), res, 0);
        return res;
    }
    
    public void helper(char[] chs, List<String> res, int pos) {
        if (pos == chs.length) {
            res.add(new String(chs));
            return;
        }
        if (chs[pos] >= '0' && chs[pos] <= '9') {
            helper(chs, res, pos + 1);
            return;
        }
        
        chs[pos] = Character.toLowerCase(chs[pos]);
        helper(chs, res, pos + 1);
        
        chs[pos] = Character.toUpperCase(chs[pos]);
        helper(chs, res, pos + 1);
    }

    public String List_array_to_String(List<String> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + list.get(0);
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + list.get(i);
        }

        return resultStr + "]";
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String S = args.replace("\"", "").replace("[[", "").replace("]]", "").trim();

        System.out.println("S = " + S);

        long start = System.currentTimeMillis();

        List<String> result = letterCasePermutation(S);

        long end = System.currentTimeMillis();

        System.out.println("result = " + List_array_to_String(result));
        System.out.println((end - start)  + "ms\n");
    }
}

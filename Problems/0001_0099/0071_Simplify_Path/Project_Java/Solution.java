import java.util.*;

public class Solution {
    public String simplifyPath(String path) {
        // 4ms
        Stack<String> stack = new Stack<>();
        String[] flds = path.split("/");

        for (String fld : flds) {
            if (fld.equals("") || fld.equals(".")) {
                continue;
            } else if (fld.equals("..")) {
                if (stack.size() > 0) {
                    stack.pop();
                }
            } else {
                stack.push(fld);
            }
        }

        StringBuilder res = new StringBuilder("/");
        for (int i = 0 ; i < stack.size(); i++) {
            res.append(stack.get(i) + "/");
        }

        if (res.length() <= 1)
            return "/";
        return res.delete(res.length() - 1, res.length()).toString();
    }

    public void Main(String temp) {
        String path = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("path = " + path);

        long start = System.currentTimeMillis();
        
        String result = simplifyPath(path);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}

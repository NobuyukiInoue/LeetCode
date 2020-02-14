import java.util.*;

public class Solution {
    public String removeOuterParentheses(String S) {
        // 2ms
        StringBuilder res = new StringBuilder(S.length() / 2);
        int openParens = 0;
        
        for (char c : S.toCharArray()) {
            switch(c) {
                case '(':
                    if(openParens != 0)
                        res.append(c);
                    openParens++;
                    break;
                    
                case ')':
                    openParens--;
                    if(openParens != 0)
                        res.append(c);
                    break;
            }
        }
        
        return res.toString();   
    }

    public String removeOuterParentheses2(String S) {
        // 3ms
        //StringBuffer res = new StringBuffer();
        StringBuilder res = new StringBuilder();
        int opened = 0;

        for (char ch : S.toCharArray()) {
            if (ch == '(' && opened > 0)
                res.append(String.valueOf(ch));
            if (ch == ')' && opened > 1)
                res.append(String.valueOf(ch));

            if (ch == '(')
                opened++;
            else
                opened--;
        }
        return res.toString();
    }

    private String string_array_to_string(String[] words)
    {
        if (words.length <= 0)
            return "";

        String resultStr = words[0];
        for (int i = 1; i < words.length; ++i)
            resultStr += "," + words[i];

        return resultStr;
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

    public void Main(String temp) {
        String S = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("S = " + S);

        long start = System.currentTimeMillis();
        
        String result = removeOuterParentheses(S);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

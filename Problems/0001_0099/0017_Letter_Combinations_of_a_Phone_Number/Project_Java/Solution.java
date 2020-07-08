import java.util.*;

public class Solution {
    private static final Map<Character, String> mapping = new HashMap<>();
    static { 
        mapping.put('2', "abc"); mapping.put('3', "def"); 
        mapping.put('4', "ghi"); mapping.put('5', "jkl"); 
        mapping.put('6', "mno"); mapping.put('7', "pqrs");
        mapping.put('8', "tuv"); mapping.put('9', "wxyz");
    }

    public List<String> letterCombinations(String digits) {
        // 1ms
        List<String> res = new LinkedList<>();

        if (digits.isEmpty())
            return res;

        char[] buf = new char[digits.length()];
        for (int k = 0; k < buf.length; k++) {
                buf[k] = mapping.get(digits.charAt(k)).charAt(0);
        }

        int[] idx = new int[digits.length()];
        int i = 0;
        while (i < digits.length()) {
            res.add(new String(buf));
            i = 0;
            while (i < digits.length()) {
                idx[i] = (idx[i] + 1) % mapping.get(digits.charAt(i)).length();
                buf[i] = mapping.get(digits.charAt(i)).charAt(idx[i]);
                if (idx[i] != 0) {
                    break;
                }
                i++;
            }
        }
        return res;
    }

    public String listStringArrayToString(List<String> list) {
        if (list.size() <= 0)
            return "[]";

        StringBuilder resultStr = new StringBuilder("[" + list.get(0));
        for (int i = 1; i < list.size(); i++) {
            resultStr.append(", " + list.get(i));
        }

        resultStr.append("]");
        return resultStr.toString();
    }

    public void Main(String temp) {
        String digits = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("digits = " + digits);

        long start = System.currentTimeMillis();

        List<String> result = letterCombinations(digits);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

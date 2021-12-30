import java.util.*;

public class Solution {
    public String reformatNumber2(String number) {
        // 7ms
        return number.replaceAll("\\D", "").replaceAll("...?(?=..)", "$0-");
    }

    public String reformatNumber(String number) {
        // 1ms
        LinkedList<Character> list = new LinkedList<Character>();
        int i, n = number.length();
        char ch;
        
        for (i = 0; i < n; i++) {
            ch = number.charAt(i);
            if (ch >= '0' && ch <= '9') {
                list.addLast(ch);
            }
        }
        
        StringBuilder builder = new StringBuilder();
        
        while (list.size() > 4) {
            for (i = 0; i < 3; i++) {
                builder.append(list.pollFirst());
            }
            
            if (!list.isEmpty()) {
                builder.append("-");
            }
        }
        
        if (list.size() < 4) {
            while (!list.isEmpty()) {
                builder.append(list.pollFirst());
            }
        } else {
            builder.append(list.pollFirst());
            builder.append(list.pollFirst());
            builder.append("-");
            builder.append(list.pollFirst());
            builder.append(list.pollFirst());
        }
        return builder.toString();
    }

    public void Main(String temp) {
        String number = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("number = " + number);

        long start = System.currentTimeMillis();

        String result = reformatNumber(number);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

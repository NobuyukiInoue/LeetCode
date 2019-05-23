import java.util.*;

public class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> set = new HashSet<>();
        for(String email : emails) {
            StringBuilder sb = new StringBuilder();
            for(char c: email.toCharArray()) {
                if (c == '.')
                    continue;
                if (c == '+')
                    break;
                if (c == '@')
                    break;
                sb.append(c);
            }
            String cur = sb.toString() + email.substring(email.indexOf('@'));
            set.add(cur);
        }
        return set.size();
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

    public void Main(String temp) {
        String[] emails = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        System.out.println("emails = " + string_array_to_string(emails));

        long start = System.currentTimeMillis();
        
        int result = numUniqueEmails(emails);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

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

    public void Main(String temp) {
        String[] emails = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        Mylib ml = new Mylib();
        System.out.println("emails = " + ml.stringArrayToString(emails));

        long start = System.currentTimeMillis();

        int result = numUniqueEmails(emails);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public boolean strongPasswordCheckerII(String password) {
        // 2ms - 3ms
        Set<Character> seen = new HashSet<>();
        for (int i = 0; i < password.length(); ++i) {
            char c = password.charAt(i);
            if (i > 0 && c == password.charAt(i - 1)) {
                return false;
            }
            if (Character.isLowerCase(c)) {
                seen.add('l');
            } else if (Character.isUpperCase(c)) {
                seen.add('u');
            } else if (Character.isDigit(c)) {
                seen.add('d');
            } else if ("!@#$%^&*()-+".contains(c + "")) {
                seen.add('s');
            }
        }
        return password.length() >= 8 && seen.size() == 4;
    }

    public void Main(String temp) {
        String password = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("password = " + password);

        long start = System.currentTimeMillis();

        boolean result = strongPasswordCheckerII(password);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

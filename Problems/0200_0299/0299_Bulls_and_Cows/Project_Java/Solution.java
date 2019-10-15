import java.util.*;

public class Solution {
    public String getHint(String secret, String guess) {
        // 1ms
        int a = 0, b = 0;
        int[] digits = new int[10];
        for(int i = 0; i < secret.length(); i++) {
            if (secret.charAt(i) == guess.charAt(i))
                a++;
            else {
                if (++digits[secret.charAt(i)-'0'] <= 0)
                    b++;
                if (--digits[guess.charAt(i)-'0'] >= 0)
                    b++;
            }
        }
        return a + "A" + b + "B";
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("[", "").replace("]", "").trim().split(",");

        String secret = flds[0];
        String guess = flds[1];
        System.out.println("secret = " + secret + ", guess = " + guess);

        long start = System.currentTimeMillis();
        
        String result = getHint(secret, guess);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

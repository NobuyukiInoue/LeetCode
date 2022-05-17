import java.util.*;

public class Solution {
    public String removeDigit(String number, char digit) {
        char[] chars = number.toCharArray();
        StringBuilder str = new StringBuilder(number);
        int position = -1;
        for (int i = 0; i < chars.length - 1; i++) {
            if (chars[i] == digit && chars[i] < chars[i + 1]) {
                position = i;
                break;
            }
        }
        if (position == -1) {
            return str.deleteCharAt(number.lastIndexOf(digit)).toString();
        } else {
            return str.deleteCharAt(position).toString();
        }
    }

    public String removeDigit2(String number, char digit) {
        // 3ms
        String ans = "0";
        for (int i = 0; i < number.length(); i++) {
            if (number.charAt(i) == digit) {
                ans = myMax(ans, number.substring(0, i) + number.substring(i+1));
            }
        }
        return ans;
    }

    private String myMax(String a, String b) {
        if (a.length() > b.length()) {
            return a;
        } else if (b.length() > a.length()) {
            return b;
        } else {
            for (int i = 0; i < a.length(); i++) {
                if (a.charAt(i) > b.charAt(i)) {
                    return a;
                } else if (b.charAt(i) > a.charAt(i)) {
                    return b;
                }
            }
            return a;
        }
    }

    public String removeDigit_List(String number, char digit) {
        // 4ms
        List<String> digits = new ArrayList<>();
        for (int i = 0; i < number.length(); i++) {
            if (number.charAt(i) == digit) {
                String stringWithoutDigit = number.substring(0, i) + number.substring(i + 1);
                digits.add(stringWithoutDigit);
            }
        }        
        Collections.sort(digits);
        return digits.get(digits.size() - 1);
    }

/*
    // 10ms
    import java.math.*;

    public String removeDigit(String number, char digit) {
        String res = String.valueOf(Integer.MIN_VALUE);
        for(int i = 0; i < number.length(); i++) {
            StringBuilder str = new StringBuilder(number);
            if (str.charAt(i) == digit) {
                String ans = str.deleteCharAt(i).toString();
                BigInteger resold = new BigInteger(res);
                BigInteger resnew = new BigInteger(ans);
                res = (String.valueOf(resold.compareTo(resnew)).equals("-1"))? ans: res;
            }
        }
        return res;
    }
*/

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").trim().split(",");

        String number = flds[0];
        char digit = flds[1].charAt(0);
        System.out.println("number = " + number + ", digit = " + digit);

        long start = System.currentTimeMillis();

        String result = removeDigit(number, digit);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

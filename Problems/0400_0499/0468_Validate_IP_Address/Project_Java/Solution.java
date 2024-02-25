import java.util.*;

public class Solution {
    public String validIPAddress(String queryIP) {
        // 3ms - 4ms
        String[] ipv4 = queryIP.split("\\.",-1);
        String[] ipv6 = queryIP.split("\\:",-1);
        if (queryIP.chars().filter(ch -> ch == '.').count() == 3) {
            for (String s : ipv4) {
                if (isIPv4(s)) {
                    continue;
                } else {
                    return "Neither";
                }
            }
            return "IPv4";
        }
        if (queryIP.chars().filter(ch -> ch == ':').count() == 7) {
            for (String s : ipv6) {
                if(isIPv6(s)) {
                    continue;
                } else {
                    return "Neither";
                }
            }
            return "IPv6";
        }
        return "Neither";
    }

    public static boolean isIPv4 (String s) {
        try {
            return String.valueOf(Integer.valueOf(s)).equals(s) && Integer.parseInt(s) >= 0 && Integer.parseInt(s) <= 255;
        }
        catch (NumberFormatException e) {
            return false;
        }
    }

    public static boolean isIPv6 (String s) {
        if (s.length() > 4) {
            return false;
        }
        try {
            return Integer.parseInt(s, 16) >= 0 && s.charAt(0) != '-';
        }
        catch (NumberFormatException e) {
            return false;
        }
    }

    public void Main(String temp) {
        String queryIP = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("queryIP = \"" + queryIP + "\"");

        long start = System.currentTimeMillis();

        String result = validIPAddress(queryIP);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}

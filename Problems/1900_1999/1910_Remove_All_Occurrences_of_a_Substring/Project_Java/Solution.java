import java.util.*;

public class Solution {
    public String removeOccurrences(String s, String part) {
        // 1ms
        int pos = s.indexOf(part);
        while (pos >= 0) {
            s = s.substring(0, pos) + s.substring(pos + part.length());
            pos = s.indexOf(part);
        }
        return s;
    }

    public String removeOccurrences2(String s, String part) {
        // 1ms
		StringBuilder sb = new StringBuilder(s);
		while (sb.indexOf(part) != -1) {
			sb.delete(sb.indexOf(part), sb.indexOf(part)+part.length());
		}
		return sb.toString();
	}

    public String removeOccurrences3(String s, String part) {
        // 10ms
        while (s.contains(part)) {
            s = s.replaceFirst(part, "");
        }
        return s;
    }

    /*
    public String removeOccurrences(String s, String part) {
        // 10ms
        return s.contains(part) ? removeOccurrences(s.replaceFirst(part, ""), part) : s;
    }
    */

    public void Main(String temp) {
        String[] flds = temp.replace(", ", ",").replace("\"", "").replace("[[", "").replace("]]", "").split("\\],\\[");

        String s = flds[0];
        String part = flds[1];

        System.out.println("s = \"" + s + "\", part = " + part + "\"");
        long start = System.currentTimeMillis();

        String result = removeOccurrences(s, part);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}

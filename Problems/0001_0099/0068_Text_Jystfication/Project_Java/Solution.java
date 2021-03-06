import java.util.*;

public class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> result = new ArrayList<>();
        int end = 0;
        while(end < words.length) {
            int sum = 0;
            int start = end;
            while(end < words.length && sum + words[end].length() <= maxWidth) {
                sum += words[end].length() + 1;
                end++;
            }
            StringBuffer newString = new StringBuffer();
            if(end >= words.length) {
                for(int i = start; i < end - 1; i++) {
                    newString.append(words[i]);
                    newString.append(" ");
                }
                newString.append(words[end - 1]);
                int count = maxWidth - newString.length();
                for(int j = 0; j < count; j++) {
                    newString.append(" ");
                }
                result.add(newString.toString());
                continue;
            }
            int spaces = maxWidth - sum;
            spaces += end - start;
            int noOfGaps = end - start - 1;
            if(noOfGaps == 0) {
                newString.append(words[end - 1]);
                
                for(int j = 0; j < maxWidth - words[end - 1].length(); j++) {
                    newString.append(" ");
                }
                result.add(newString.toString());
                continue;
            }
            int spaceBetweenWords = spaces / noOfGaps;
            int extraSpaces = spaces % noOfGaps;

            for(int i = start; i < end - 1; i++) {
                newString.append(words[i]);
                for(int j = 0; j < spaceBetweenWords; j++) {
                    newString.append(" ");
                }
                if(extraSpaces > 0) {
                    newString.append(" ");
                    extraSpaces--;
                }
            }
            newString.append(words[end - 1]);
            result.add(newString.toString());
        }
        return result;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String[] words = flds[0].split(",");
        int maxWidth = Integer.parseInt(flds[1]);

        Mylib ml = new Mylib();
        System.out.println("words[] = " + ml.stringArrayToString(words));
        System.out.println("maxWidth = " + String.valueOf(maxWidth));

        long start = System.currentTimeMillis();

        List<String> result = fullJustify(words, maxWidth);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

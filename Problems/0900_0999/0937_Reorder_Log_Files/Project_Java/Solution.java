import java.util.*;

public class Solution {
    public String[] reorderLogFiles(String[] logs) {
        List<String> letterLog = new ArrayList<>();
        List<String> digitLog = new ArrayList<>();
        
        // seperate digit and letter logs
        for (String log : logs) {
            String[] tokenized = log.split(" ", 2);
            if (!isInteger(tokenized[1]))
                letterLog.add(log);
            else
                digitLog.add(log);
        }
        
        // sort letter logs lexaographically by comparing first token in log
        Collections.sort(letterLog, new Comparator<String>() {
            public int compare(String s1, String s2) {
                String[] sp1 = s1.split(" ", 2);
                String[] sp2 = s2.split(" ", 2);
                return (sp1[1].compareTo(sp2[1]) == 0) ? sp1[0].compareTo(sp2[0]) : sp1[1].compareTo(sp2[1]);
            }
        });
        
        // merge lists
        String[] out = new String[logs.length];
        int i, j;
        
        for (i = 0; i < letterLog.size(); i++)
            out[i] = letterLog.get(i);

        for (j = 0; j < digitLog.size(); j++)
            out[i + j] = digitLog.get(j);

        return out;
    }
    
    boolean isInteger(String word) {
        return (word.charAt(0) >= '0' && word.charAt(0) <= '9');
    }

    public String output_str_array(String[] words) {
        String result = "[";

        for (int i = 0; i < words.length; i++) {
            if (i == 0) {
                result += "\"" + words[i] + "\"";
            } else {
                result += ",\"" + words[i] + "\"";
            }
        }

        return result + "]";
    }

    public void Main(String temp) {
        String[] logs = temp.replace("\"", "").replace("[", "").replace("]", "").trim().split(",");
        System.out.println("logs = " + output_str_array(logs));

        long start = System.currentTimeMillis();
        
        String[] result = reorderLogFiles(logs);

        long end = System.currentTimeMillis();

        System.out.println("result = " + output_str_array(result));
        System.out.println((end - start)  + "ms\n");
    }
}

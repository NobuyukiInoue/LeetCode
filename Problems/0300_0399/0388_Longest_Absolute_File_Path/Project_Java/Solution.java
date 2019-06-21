import java.util.*;

public class Solution {
    public int lengthLongestPath(String input) {
        String[] paths = input.split("\n");
        int[] stack = new int[paths.length+1];
        int maxLen = 0;
        for(String s:paths){
            int lev = s.lastIndexOf("\t") + 1;
            int curLen = stack[lev+1] = stack[lev] + s.length() - lev + 1;
            if (s.contains("."))
                maxLen = Math.max(maxLen, curLen-1);
        }
        return maxLen;
    }

    public void Main(String temp) {
        String input = temp.replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("input = " + input);

        long start = System.currentTimeMillis();
        
        int result = lengthLongestPath(input);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

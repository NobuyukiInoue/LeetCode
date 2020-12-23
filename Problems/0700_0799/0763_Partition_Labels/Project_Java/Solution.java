import java.util.*;

public class Solution {
    public List<Integer> partitionLabels(String S) {
        // 3ms
        List<Integer> res = new ArrayList<>();
        int[] rightMostPos = new int[26];
        Arrays.fill(rightMostPos, -1);
        
        for (int i = 0; i < S.length(); ++i) {
            rightMostPos[S.charAt(i) - 'a'] = i;
        }
        
        int currRight = -1, count = 0;
        for (int i = 0; i < S.length(); ++i) {
            count++;
            currRight = Math.max(currRight, rightMostPos[S.charAt(i) - 'a']);
             if (i == currRight) {
                res.add(count);
                count = 0;
            }
        }
        
        return res;
    }

    public List<Integer> partitionLabels2(String S) {
        // 8ms
        HashMap<Character, Integer> first_sight = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < S.length(); i++) {
            char ch = S.charAt(i);
            if (!first_sight.containsKey(ch)) {
                first_sight.put(ch, i);
            }
            int sub_start = i;
            while (sub_start > first_sight.get(ch)) {
                sub_start = stack.pop();
            }
            stack.push(sub_start);
        }
        stack.push(S.length());
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < stack.size() - 1; i++) {
            res.add(stack.get(i + 1) - stack.get(i));
        }
        return res;
    }

    public void Main(String temp) {
        String S = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("S = " + S);

        long start = System.currentTimeMillis();

        List<Integer> result = partitionLabels(S);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

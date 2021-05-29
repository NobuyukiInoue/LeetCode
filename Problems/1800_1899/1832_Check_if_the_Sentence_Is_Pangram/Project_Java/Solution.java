import java.util.*;

public class Solution {
    public boolean checkIfPangram(String sentence) {
        // 1ms
        HashMap<Character, Boolean> cnts = new HashMap<>();
        int count = 0;
        for (char ch : sentence.toCharArray()) {
            if (!cnts.containsKey(ch)) {
                cnts.put(ch, true);
                if (++count >= 26) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean checkIfPangram1(String sentence) {
        // 3ms
        Set<Character> s = new HashSet<>();
        for (int i = 0; i < sentence.length(); ++i) {
            s.add(sentence.charAt(i));
        }
        return s.size() == 26;
    }

    public void Main(String temp) {
        String sentence = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("sentence = " + sentence);

        long start = System.currentTimeMillis();

        boolean result = checkIfPangram(sentence);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

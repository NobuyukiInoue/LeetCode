import java.util.*;
import java.util.stream.Collectors;

public class Solution {

    public String frequencySort(String s) {
        // 13ms
        HashMap<Character, Integer> hashMap = new HashMap<>();
        for (char c : s.toCharArray()) {
            hashMap.put(c, hashMap.getOrDefault(c, 0) + 1);
        }
        return hashMap.entrySet().stream().sorted((o1, o2) -> Integer.compare(o2.getValue(), o1.getValue()))
                      .map(entry -> {
                          char[] chars = new char[entry.getValue()];
                          Arrays.fill(chars, entry.getKey());
                          return String.valueOf(chars);
                      }).collect(Collectors.joining());
    }

    int max;

    public String frequencySort2(String s) {
        // 4ms
        int[] m = new int[123];

        for (char c: s.toCharArray()) {
            m[c]++;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 123; i++) {
            getMaxIndex(m);
            if (max == 1) {
                break;
            }
            for (int j = 0; j < m[max]; j++) {
                sb.append((char)max);
            }
            m[max] = 0;
        }

        for (int i = 0; i < 123; i++) {
            if (m[i] == 1) {
                sb.append((char)i);
            }
        }

        return sb.toString();
    }

    public int getMaxIndex(int[] m) {
        max = 0;

        for (int i = 1; i < 123; i++) {
            if (m[i] > m[max]) {
                max = i;
            }
        }

        return max;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        String result = frequencySort(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

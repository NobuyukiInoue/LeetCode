import java.util.*;

public class Solution {
    public String reorganizeString(String S) {
        // 2ms
        int[] counts = new int[26];
        for (char ch : S.toCharArray()) {
            counts[ch - 'a'] += 1;
        }

        Comparator<int[]> comp = new Comparator<int[]>() {
            public int compare(int[] a1, int[] a2) {
                return a2[0] - a1[0];
            }
        };
        int limit = (S.length()+ 1)/2;
        PriorityQueue<int[]> pq = new PriorityQueue(comp);
        for (int i = 0; i < counts.length; i++) {
            if (counts[i] > limit) {
                return "";
            }
            if (counts[i] > 0) {
                pq.add(new int[] {counts[i], 'a' + i});
            }
        }

        StringBuilder sb = new StringBuilder();
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            if (sb.length() == 0 || sb.charAt(sb.length() - 1) != (char)cur[1]) {
                sb.append((char)cur[1]);
                if (cur[0] > 1) {
                    cur[0] -= 1;
                    pq.add(cur);
                }
            } else {
                int[] p = pq.poll();
                sb.append((char)p[1]);
                if (p[0] > 1) {
                    p[0] -= 1;
                    pq.add(p);
                }
                pq.add(cur);
            }
        }
        return sb.toString();
    }

    public String reorganizeString2(String s) {
        // 3ms
        Map<Character, Integer> map = new HashMap<>();
        for (char c : s.toCharArray()) {
            int count = map.getOrDefault(c, 0) + 1;
            if (count > (s.length() + 1) / 2) {
                return "";
            }
            map.put(c, count);
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> b[1] - a[1]);
        for (char c : map.keySet()) {
            pq.add(new int[] {c, map.get(c)});
        }

        StringBuilder sb = new StringBuilder();
        while (!pq.isEmpty()) {
            int[] first = pq.poll();
            if (sb.length() == 0 || first[0] != sb.charAt(sb.length() - 1)) {
                sb.append((char) first[0]);
                if (--first[1] > 0) {
                    pq.add(first);
                }
            } else {
                int[] second = pq.poll();
                sb.append((char) second[0]);
                if (--second[1] > 0) {
                    pq.add(second);
                }
                pq.add(first);
            }
        }
        return sb.toString();
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        String result = reorganizeString(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

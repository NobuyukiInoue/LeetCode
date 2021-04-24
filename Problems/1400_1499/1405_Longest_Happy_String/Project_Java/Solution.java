import java.util.*;

public class Solution {
	public String longestDiverseString(int a, int b, int c) {
        // 1ms
		PriorityQueue<int[]> queue = new PriorityQueue<>((x, y) -> y[0] - x[0]);
		if (a > 0) {
            queue.add(new int[] {a, 0});
        }
		if (b > 0) {
            queue.add(new int[] {b, 1});
        }
		if (c > 0) {
            queue.add(new int[] {c, 2});
        }

		StringBuilder sb = new StringBuilder();
		while (!queue.isEmpty()) {
			int[] p1 = queue.poll();
			char c1 = (char) ('a' + p1[1]);
			if (p1[0] > 1) {
				sb.append(c1).append(c1);
				p1[0] -= 2;
			} else {
				sb.append(c1);
				p1[0] -= 1;
			}
			if (queue.isEmpty()) {
                break;
            }

            int[] p2 = queue.poll();
			char c2 = (char) ('a' + p2[1]);
			if (p2[0] > 1 && p2[0] >= p1[0]) {
				sb.append(c2).append(c2);
				p2[0] -= 2;
			} else {
				sb.append(c2);
				p2[0] -= 1;
			}
			if (p1[0] > 0) {
                queue.add(p1);
            }
			if (p2[0] > 0) {
                queue.add(p2);
            }
		}
		return sb.toString();
    }

    public String longestDiverseString2(int a, int b, int c) {
        // 8ms
        return generate(a, b, c, "a", "b", "c");
    }

    String generate(int a, int b, int c, String aa, String bb, String cc) {
        if (a < b) {
            return generate(b, a, c, bb, aa, cc);
        }
        if (b < c) {
            return generate(a, c, b, aa, cc, bb);
        }
        if (b == 0) {
            return aa.repeat(Math.min(2, a));
        }
        int use_a = Math.min(2, a);
        int use_b = a - use_a >= b ? 1 : 0;
        return aa.repeat(use_a) + bb.repeat(use_b) + generate(a - use_a, b - use_b, c, aa, bb, cc);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim().split(",");

        int a = Integer.parseInt(flds[0]);
        int b = Integer.parseInt(flds[1]);
        int c = Integer.parseInt(flds[2]);
        System.out.println("a = " + Integer.toString(a) + ", b = " + Integer.toString(b) + ", c = " + Integer.toString(c));

        long start = System.currentTimeMillis();

        String result = longestDiverseString(a, b, c);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

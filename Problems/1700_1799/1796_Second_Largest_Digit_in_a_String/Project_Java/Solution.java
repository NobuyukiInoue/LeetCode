import java.util.*;

public class Solution {
    public int secondHighest2(String s) {
        // 2ms
        ArrayList<Integer> nums = new ArrayList<>();
        for (char ch : s.toCharArray()) {
            if ('0' <= ch && ch <= '9') {
                if (!nums.contains(ch - '0')) {
                    nums.add(ch - '0');
                }
            }
        }
        if (nums.size() < 2)
            return -1;
        Collections.sort(nums);
        return nums.get(nums.size() - 2);
    }

    public int secondHighest(String s) {
        // 1ms
        int firstLargest = -1;
        int secondLargest = -1;
        for (int i = 0;i < s.length(); i++) {
            if (Character.isDigit(s.charAt(i))) {
                int d = s.charAt(i) - '0';
                if (d > firstLargest) {
                    secondLargest = firstLargest;
                    firstLargest = d;
                } else if (d > secondLargest && d < firstLargest) {
                    secondLargest = d;
                }
            }
        }
        return secondLargest;
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = secondHighest(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

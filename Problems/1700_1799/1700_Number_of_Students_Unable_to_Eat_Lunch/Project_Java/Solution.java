import java.util.*;

public class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        // 1ms
        HashMap<Integer, Integer> cnt = new HashMap<>();
        for (int n : students) {
            cnt.put(n, cnt.getOrDefault(n, 0) + 1);
        }

        int n = students.length;
        int k = 0;

        if (cnt.get(sandwiches[k]) == null) {
            return n;
        }

        while (k < n && cnt.get(sandwiches[k]) > 0) {
            cnt.put(sandwiches[k], cnt.get(sandwiches[k]) - 1);
            k++;
        }

        return n - k;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] students   = ml.stringToIntArray(flds[0]);
        int[] sandwiches = ml.stringToIntArray(flds[1]);
        System.out.println("students   = " + ml.intArrayToString(students));
        System.out.println("sandwiches = " + ml.intArrayToString(sandwiches));

        long start = System.currentTimeMillis();

        int result = countStudents(students, sandwiches);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

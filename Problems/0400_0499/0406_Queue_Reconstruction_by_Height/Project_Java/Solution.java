import java.util.*;

public class Solution {
    public int[][] reconstructQueue(int[][] people) {
        // 5ms
        Arrays.sort(people, (p1, p2) -> p1[0] == p2[0] ? p1[1] - p2[1] : p2[0] - p1[0]); 
        List<int[]> list = new ArrayList<>();
        for (int i = 0; i < people.length; i++) {
            list.add(people[i][1], people[i]);
        }
        return list.toArray(people);
    }

    private String intIntArrayToString(int[][] matrix) {
        if (matrix.length <= 0) {
            return "[]";
        }

        Mylib ml = new Mylib();
        StringBuilder sb = new StringBuilder("[\n");
        sb.append("  " + ml.intArrayToString(matrix[0]) + "\n");
        for (int i = 1; i < matrix.length; i++) {
            sb.append(", " + ml.intArrayToString(matrix[i]) + "\n");
        }
        sb.append("]");
        return sb.toString();
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        String[] str_people = flds.split("\\],\\[");
        Mylib ml = new Mylib();
        int[][] people = new int[str_people.length][];
            for (int i = 0; i < str_people.length; i++) {
            people[i] = ml.stringTointArray(str_people[i]);
        }

        System.out.println("poeple = " + intIntArrayToString(people));
        long start = System.currentTimeMillis();

        int[][] result = reconstructQueue(people);

        long end = System.currentTimeMillis();

        System.out.println("result = " + intIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

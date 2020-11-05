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

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_people = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] people = ml.stringToIntIntArray(str_people);
        System.out.println("poeple = " + ml.intIntArrayToString(people));

        long start = System.currentTimeMillis();

        int[][] result = reconstructQueue(people);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

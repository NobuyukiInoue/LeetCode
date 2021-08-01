import java.util.*;

public class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        // 8ms
        HashMap<Integer, Integer> count_map = new HashMap<>();
        for (List<Integer> row : wall) {
            int pos = 0;
            for (int i = 0; i < row.size() - 1; i++) {
                pos += row.get(i);
                count_map.put(pos, count_map.getOrDefault(pos, 0) + 1);
            }
        }
        int max_pos = 0;
        for (int n : count_map.values()) {
            max_pos = Math.max(max_pos, n);
        }
        return wall.size() - max_pos;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        List<List<Integer>> wall = ml.stringArrayToListListIntArray(flds);
        System.out.println("wall = " + ml.listListIntArrayToString(wall));

        long start = System.currentTimeMillis();

        int result = leastBricks(wall);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

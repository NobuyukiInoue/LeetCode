import java.util.*;

public class Solution {
    // 1ms
    HashMap<Integer, Boolean> visited;

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        visited = new HashMap<>();
        dfs(rooms, 0);
        return visited.size() == rooms.size();
    }

    private void dfs(List<List<Integer>> rooms, int room) {
        if (visited.containsKey(room) == false) { 
            visited.put(room, true);
            if (rooms.get(room) != null) {
                for (int key : rooms.get(room)) {
                    dfs(rooms, key);
                }
            }
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace("[]", "[null]").replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        List<List<Integer>> rooms = new ArrayList<>();
        for (int i = 0; i < flds.length; i++) {
            List<Integer> room = new ArrayList<>();
            if (!flds[i].equals("null")) {
                int[] keys = ml.stringToIntArray(flds[i]);
                if (keys != null) {
                    for (int key:keys) {
                        room.add(key);
                    }
                }
            }
            rooms.add(room);
        }

        System.out.println("rooms = " + ml.listListIntArrayToString(rooms));

        long start = System.currentTimeMillis();

        boolean result = canVisitAllRooms(rooms);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

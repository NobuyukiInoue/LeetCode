import java.util.*;

public class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        // 6ms
        if (buildings == null || buildings.length == 0)
            return new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return a[2] != b[2] ? b[2] - a[2] : b[1] - a[1];
            }
        });
        
        for (int[] building : buildings) {
            while (!pq.isEmpty() && pq.peek()[1] < building[0]) {
                savePollRes(res, pq);
            }
            if (pq.isEmpty()) {
                res.add(Arrays.asList(building[0], building[2]));
            } else if (pq.peek()[2] < building[2]) {
                if (res.get(res.size() - 1).get(0) == building[0]) {
                    res.remove(res.size() - 1);
                }
                res.add(Arrays.asList(building[0], building[2]));
            }
            pq.add(building);
        }
        while (!pq.isEmpty()) {
            savePollRes(res, pq);
        }
        return res;
    }
    
    private void savePollRes(List<List<Integer>> res, PriorityQueue<int[]> pq) {
        int[] previous = pq.poll();
        int[] peek = pq.peek();
        while (peek != null && previous[2] >= peek[2] && previous[1] >= peek[1]) {
			pq.poll();
			peek = pq.peek();
        }

        if (peek == null) {
             res.add(Arrays.asList(previous[1], 0));
        } else {
             res.add(Arrays.asList(previous[1], peek[2]));
        }
    }

    public String intArrayToString(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";

            if (data[i] == -1)
                result += "null";
            else
                result += Integer.toString(data[i]);
        }
    
        return result;
    }

    public String listArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] buildings = new int[flds.length][];
        System.out.print("buildings = [");
        for (int i = 0; i < flds.length; i++) {
            buildings[i] = ml.str_to_int_array(flds[i]);
            if (i == 0)
                System.out.print("[" + intArrayToString(buildings[i]) + "]");
            else
                System.out.print(", [" + intArrayToString(buildings[i]) + "]");
        }
        System.out.println("]");

        long start = System.currentTimeMillis();

        List<List<Integer>> result = getSkyline(buildings);

        long end = System.currentTimeMillis();

        System.out.println("result = [");
        for (int i = 0; i < result.size(); i++) {
            if (i == 0)
                System.out.println("  " + listArrayToString(result.get(i)));
            else
                System.out.println(", " + listArrayToString(result.get(i)));
        }
        System.out.println("]");

        System.out.println((end - start)  + "ms\n");
    }
}

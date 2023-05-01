import java.util.*;

public class Solution {
    public boolean pyramidTransition(String bottom, List<String> allowed) {
        // 489ms - 490ms
        final int[][] pyramid = new int[8][8];
        final int depth = bottom.length() - 1;
        for (int i = 0; i < bottom.length(); i++) {
            pyramid[depth][i] = bottom.charAt(i) - 'A';
        }
        final boolean[][][] candidates = new boolean[7][7][7];
        for (String a : allowed) {
            candidates[a.charAt(0) - 'A'][a.charAt(1) - 'A'][a.charAt(2) - 'A'] = true;
        }
        return dfs(pyramid, depth, 0, candidates);
    }

    private boolean dfs(int[][] pyramid, int depth, int index, boolean[][][] candidates) {
        if (depth == 0 && index == 0) {
            return true;
        }
        if (depth == index) {
            return dfs(pyramid, depth - 1, 0, candidates);
        }
        final int first = pyramid[depth][index];
        final int second = pyramid[depth][index + 1];
        for (int i = 0; i < 7; i++) {
            if (candidates[first][second][i]) {
                pyramid[depth - 1][index] = i;
                if (dfs(pyramid, depth, index + 1, candidates)) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean pyramidTransition2(String bottom, List<String> allowed) {
        // 1715ms - 1718ms
        Map<String, List<String>> map = new HashMap<>();
        for (String s : allowed) {
            String key = s.substring(0,2);
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<String>());
            }
            map.get(key).add(s.substring(2));
        }
        return helper(bottom, map);
    }
    
    private boolean helper(String bottom, Map<String, List<String>> map) {
        if (bottom.length() == 1) {
            return true;
        }
        for (int i = 0; i<bottom.length() - 1; i++) {
            if (!map.containsKey(bottom.substring(i, i + 2))) {
                return false;
            }
        }
        List<String> ls = new ArrayList<>();
        getList(bottom, 0, new StringBuilder(), ls, map);
        for (String s : ls) {
            if (helper(s, map)) return true;
        }
        return false;
    }
    
    private void getList(String bottom, int idx, StringBuilder sb, List<String> ls, Map<String, List<String>> map) {
        if (idx == bottom.length() - 1) {
            ls.add(sb.toString());
            return;
        }
        for (String s : map.get(bottom.substring(idx, idx+2))) {
            sb.append(s);
            getList(bottom, idx + 1, sb, ls, map);
            sb.deleteCharAt(sb.length()-1);
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace(", ", ",").replace("\"", "").replace("[[", "").replace("]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        String bottom = flds[0];
        List<String> allowed = ml.stringArrayToListStringArray(flds[1].split(","));
        System.out.println("bottom = " + bottom + ", allowed = " + ml.listStringArrayToString(allowed));

        long start = System.currentTimeMillis();

        boolean result = pyramidTransition(bottom, allowed);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

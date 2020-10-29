import java.util.*;

public class Solution {

    public int findCircleNum(int[][] M) {
        // 0ms
        int[] visited = new int[M.length];
        int count = 0;
        for (int i = 0; i < M.length; i++) {
            if (visited[i] == 0) {
                dfs(M, visited, i);
                count++;
            }
        }
        return count;
    }

    public void dfs(int[][] M, int[] visited, int i) {
        for (int j = 0; j < M.length; j++) {
            if (M[i][j] == 1 && visited[j] == 0) {
                visited[j] = 1;
                dfs(M, visited, j);
            }
        }
    }

    public String matrixToString(int[][] list) {
        if (list.length <= 0)
            return "[]";

        Mylib ml = new Mylib();
        StringBuilder sb = new StringBuilder("[\n  " + ml.intArrayToString(list[0]) + "\n");
        for (int i = 1; i < list.length; i++) {
            sb.append(" ," + ml.intArrayToString(list[i]) + "\n") ;
        }

        sb.append("]");
        return sb.toString();
    }

    public String listListArrayToString(List<List<Integer>> list) {
        if (list.size() <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[" + listArrayToString(list.get(0)));
        for (int i = 1; i < list.size(); i++) {
            sb.append("," + listArrayToString(list.get(i)));
        }

        sb.append("]");
        return sb.toString();
    }

    public String listArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";
        StringBuilder sb = new StringBuilder("[" + Integer.toString(list.get(0)));
        for (int i = 1; i < list.size(); i++) {
            sb.append("," + Integer.toString(list.get(i)));
        }
        sb.append("]");
        return sb.toString();
    }

    private String gridToString(List<List<Integer>> matrix) {
        if (matrix == null || matrix.size() <= 0)
            return "[]";
        StringBuilder sb = new StringBuilder("[");
        sb.append(listArrayToString(matrix.get(0)));
        for (int i = 1; i < matrix.size(); i++) {
            sb.append(", " + listArrayToString(matrix.get(i)));
        }
        sb.append("]");
        return sb.toString();
   }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        String[] str_M = flds.split("\\],\\[");
        Mylib ml = new Mylib();
        int[][] M = new int[str_M.length][];
            for (int i = 0; i < str_M.length; i++) {
            M[i] = ml.stringTointArray(str_M[i]);
        }

        System.out.println("M = " + matrixToString(M));

        long start = System.currentTimeMillis();

        int result = findCircleNum(M);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

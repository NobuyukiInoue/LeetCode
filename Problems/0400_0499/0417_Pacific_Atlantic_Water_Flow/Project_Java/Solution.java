import java.util.*;

public class Solution {

    public List<List<Integer>> pacificAtlantic(int[][] matrix) {
        // 4ms
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return res;
        }
        int n = matrix.length, m = matrix[0].length;
        boolean[][]pacific = new boolean[n][m];
        boolean[][]atlantic = new boolean[n][m];
        for(int i = 0; i < n; i++) {
            dfs(matrix, pacific, Integer.MIN_VALUE, i, 0);
            dfs(matrix, atlantic, Integer.MIN_VALUE, i, m - 1);
        }
        for(int i = 0; i < m; i++) {
            dfs(matrix, pacific, Integer.MIN_VALUE, 0, i);
            dfs(matrix, atlantic, Integer.MIN_VALUE, n - 1, i);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    res.add(new ArrayList<Integer>(Arrays.asList(i, j)));
                }
            }
        }
        return res;
    }

    int[][]dir = new int[][]{ {0, 1}, {0, -1}, {1, 0}, {-1, 0} };

    public void dfs(int[][]matrix, boolean[][]visited, int height, int x, int y){
        int n = matrix.length, m = matrix[0].length;
        if (x < 0 || x >= n || y < 0 || y >= m || visited[x][y] || matrix[x][y] < height)
            return;
        visited[x][y] = true;
        for(int[]d : dir){
            dfs(matrix, visited, matrix[x][y], x + d[0], y + d[1]);
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

        String[] str_matrix = flds.split("\\],\\[");
        Mylib ml = new Mylib();
        int[][] matrix = new int[str_matrix.length][];
            for (int i = 0; i < str_matrix.length; i++) {
            matrix[i] = ml.stringTointArray(str_matrix[i]);
        }

        System.out.println("matrix = " + matrixToString(matrix));

        long start = System.currentTimeMillis();

        List<List<Integer>> result = pacificAtlantic(matrix);

        long end = System.currentTimeMillis();

        System.out.println("result = " + gridToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

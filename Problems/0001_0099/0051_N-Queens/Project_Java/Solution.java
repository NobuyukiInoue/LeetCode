import java.util.*;

public class Solution {
    public List<List<String>> solveNQueens(int n) {
        // 4ms
        List<List<String>> res = new ArrayList<>();
        helper(0, new boolean[n], new boolean[2*n], new boolean[2*n], Arrays.asList(new String[n]), res);
        return res;
    }

    private void helper(int r, boolean[] cols, boolean[] d1, boolean[] d2, List<String> board, List<List<String>> res) {
        if (r == board.size()) {
              res.add(new ArrayList<String>(board));
        } else {
            for (int c = 0; c < board.size(); c++) {
                int id1 = r - c + board.size(), id2 = 2*board.size() - r - c - 1;
                if (!cols[c] && !d1[id1] && !d2[id2]) {
                    char[] row = new char[board.size()];
                    Arrays.fill(row, '.');
                    row[c] = 'Q';
                    board.set(r, new String(row));
                    cols[c] = true;
                    d1[id1] = true;
                    d2[id2] = true;
                    helper(r + 1, cols, d1, d2, board, res);
                    cols[c] = false;
                    d1[id1] = false;
                    d2[id2] = false;
                }
            }
        }
    }

    public List<List<String>> solveNQueens2(int n) {
        // 3ms
        List<List<String>> ret = new ArrayList<>();
        int[] cols = new int[n];
        for(int i = 0; i < n; i++) {
            cols[i] = -1;
         }
   
        dfs(0,cols,ret);
        return ret;
    }
    
    void dfs(int r, int[] cols, List<List<String>> ret) {
        if (r == cols.length) {
            ret.add(toStringList(cols));
            return;
        }
            
        for (int c = 0; c < cols.length; c++) {
            if (valid(r, c, cols)) {
               cols[r] = c;
               dfs(r + 1, cols, ret);
               cols[r] = -1;
            }
        }
    }
        

    boolean valid(int r2, int c2, int[] cols) {
        for (int r1 = 0; r1 < r2; r1++) {
            int c1 = cols[r1];
            if (c1 == c2)
                return false;
            if (Math.abs(c1 - c2) == Math.abs(r1 - r2))
                return false;
        }
        return true;
    }

    List<String> toStringList(int[] cols) {
        List<String> ret = new ArrayList<>();
        int n = cols.length;
        for (int r = 0; r < n; r++) {
            int col = cols[r];
            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < n; i++)  {
                if (i == col)
                    sb.append("Q");
                else sb.append(".");
            }
            ret.add(sb.toString());   
        }    
       return ret;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        List<List<String>> result = solveNQueens(n);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listListStringArrayToString(result).replace(",", ",\n").replace("[", ",\n["));
        System.out.println((end - start)  + "ms\n");
    }
}

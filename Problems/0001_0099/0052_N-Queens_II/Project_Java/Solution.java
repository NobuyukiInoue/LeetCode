import java.util.*;

public class Solution {
    int count;
    public int totalNQueens(int n) {
        // 2ms
        count = 0;
        List<List<String>> res = new ArrayList<>();
        helper(0, new boolean[n], new boolean[2*n], new boolean[2*n], Arrays.asList(new String[n]), res);

    //  return res.size();
        return count;
    }

    private void helper(int r, boolean[] cols, boolean[] d1, boolean[] d2, List<String> board, List<List<String>> res) {
        if (r == board.size()) {
        //  res.add(new ArrayList<String>(board));
            count++;
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

        int result = totalNQueens(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

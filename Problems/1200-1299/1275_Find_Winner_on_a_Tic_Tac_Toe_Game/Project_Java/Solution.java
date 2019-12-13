import java.util.*;

public class Solution {
    public String tictactoe(int[][] moves) {
        // 0ms
        int[] aRow = new int[3], aCol = new int[3], bRow = new int[3], bCol = new int[3];
        int  aD1 = 0, aD2 = 0, bD1 = 0, bD2 = 0;
        for (int i = 0; i < moves.length; ++i) {
            int r = moves[i][0], c = moves[i][1];
            if (i % 2 == 1) {
                if (++bRow[r] == 3 || ++bCol[c] == 3 || r == c && ++bD1 == 3 || r + c == 2 && ++bD2 == 3)
                    return "B";
            } else {
                if (++aRow[r] == 3 || ++aCol[c] == 3 || r == c && ++aD1 == 3 || r + c == 2 && ++aD2 == 3)
                    return "A";
            }
        }
        return moves.length == 9 ? "Draw" : "Pending";
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        int[][] moves = new int[flds.length][];
    
        for (int i = 0; i < flds.length; i++) {
            moves[i] = ml.str_to_int_array(flds[i]);
        }

        System.out.print("moves = [");
        for (int i = 0; i < moves.length; i++) {
            if (i == 0)
                System.out.print(ml.output_int_array(moves[i]));
            else
                System.out.print("," + ml.output_int_array(moves[i]));
        }
        System.out.println("]");

        long start = System.currentTimeMillis();
        
        String result = tictactoe(moves);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

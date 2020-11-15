import java.util.*;

public class Solution {
    /* My Solution */
    public String alphabetBoardPath(String target) {
        // 1ms
        String[] board = {"abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"};
        StringBuilder res = new StringBuilder();
        int x = 0, y = 0;
        for (char ch : target.toCharArray()) {
            for (int i = 0; i < board.length; i++) {
                int pos = board[i].indexOf(ch);
                if (pos >= 0) {
                    Boolean toLastRow = false;
                    if (x > i) {
                        res.append("U".repeat(x - i));
                    } else if (x < i) {
                        if (i == 5) {
                            res.append("D".repeat(4 - x));
                            toLastRow = true;
                        } else {
                            res.append("D".repeat(i - x));
                        }
                    }
                    x = i;
                    if (y > pos)
                        res.append("L".repeat(y - pos));
                    else if (y < pos)
                        res.append("R".repeat(pos - y));
                    if (toLastRow)
                        res.append("D");
                    res.append("!");
                    y = pos;
                }
            }
        }
        return res.toString();
    }

    /* Solution2 */
    public String alphabetBoardPath2(String target) {
        // 0ms
        StringBuilder sb = new StringBuilder();
        int[] prev = new int[]{0, 0};
        for (char c : target.toCharArray()) {
            int[] curr = getPos(c);
            sb.append(getPath(prev, curr));
            sb.append('!');
            prev = curr;
        }
        return sb.toString();
    }

    private int[] getPos(char c) {
        int offset = c - 'a';
        int x = offset/5;
        int y = offset%5;
        return new int[]{x, y};
    }

    private String getPath(int[] from, int[] to) {
        // TODO
        char x = to[0] >= from[0] ? 'D' : 'U';
        char y = to[1] >= from[1] ? 'R' : 'L';
        int xOff = Math.abs(to[0] - from[0]);
        int yOff = Math.abs(to[1] - from[1]);
        StringBuilder sb = new StringBuilder();
        if (x == 'U') {
            for (int i = 0; i < xOff; i++) { sb.append(x);}
            for (int i = 0; i < yOff; i++) { sb.append(y);}
        } else {
            for (int i = 0; i < yOff; i++) { sb.append(y);}
            for (int i = 0; i < xOff; i++) { sb.append(x);}
        }
        return sb.toString();
    }

    /* Solution3 */
    public String alphabetBoardPath3(String target) {
        // 0ms
        StringBuffer rv= new StringBuffer("");
        int px = 0, py = 0 ,cx, cy;
        for (int i = 0; i < target.length(); ++i) {
            int loc =target.charAt(i) - 'a';
            cx = loc/5;
            cy = loc%5;
            while (px != cx || py != cy) {
                if (px > cx) {
                    --px;
                    rv.append('U');
                } else if (px < cx && (px < 4 || py == 0)){
                     ++px;
                    rv.append('D');
                } else if (py > cy){
                     --py;
                    rv.append('L');
                } else if (py < cy){
                     ++py;
                    rv.append('R');
                }
            }
           rv.append('!');
        }
        return rv.toString();
    }

    /* Solution4 */
    public String alphabetBoardPath4(String target) {
        // 9ms
        int x = 0, y = 0;
        StringBuilder sb = new StringBuilder();
        for (char ch : target.toCharArray()) {
            int x1 = (ch - 'a') % 5, y1 = (ch - 'a') / 5;
            sb.append(String.join("", Collections.nCopies(Math.max(0, y - y1), "U")) + 
                      String.join("", Collections.nCopies(Math.max(0, x1 - x), "R")) +
                      String.join("", Collections.nCopies(Math.max(0, x - x1), "L")) +
                      String.join("", Collections.nCopies(Math.max(0, y1 - y), "D")) + "!");
              x = x1; y = y1;
            }
        return sb.toString();
    }

    public void Main(String temp) {
        String target = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("target = " + target);

        long start = System.currentTimeMillis();

        String result = alphabetBoardPath(target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

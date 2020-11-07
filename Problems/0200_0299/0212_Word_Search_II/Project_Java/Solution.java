import java.util.*;

public class Solution {
    List<String> result = new ArrayList<>();

    class TrieNode {
        TrieNode[] children;
        String word;

        public TrieNode() {
            children = new TrieNode[26];
            word = null;
        }
    }

    TrieNode root;
    public void buildTrie(String[] words){
        root = new TrieNode();

        for (String word: words) {
            TrieNode cur = root;
            for (char ch: word.toCharArray()) {
                int index = ch - 'a';
                if (cur.children[index] == null) {
                    cur.children[index] = new TrieNode();
                }
                cur = cur.children[index];
            }
            cur.word = word;
        }
    }

    public List<String> findWords(char[][] board, String[] words) {
        // 8ms
        if (words.length == 0 || words == null || board == null || board.length == 0)
            return result;

        buildTrie(words);

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                int index = board[i][j] - 'a';
                if (root.children[index] != null) {
                    dfs(board, i, j, root);
                }
            }
        }

        return result;
    }

    public void dfs(char[][] board, int i,int j, TrieNode cur){
        if (i < 0 || i >= board.length || j < 0 || j >= board[i].length)
            return;

        char ch = board[i][j];
        if (ch == '#' || cur.children[ch - 'a'] == null)
            return;

        cur = cur.children[ch - 'a'];
        if (cur.word != null) {
            result.add(cur.word);
            cur.word = null;
        }

        board[i][j] = '#';
        dfs(board, i + 1, j, cur);
        dfs(board, i - 1, j, cur);
        dfs(board, i, j + 1, cur);
        dfs(board, i, j - 1, cur);
        board[i][j] = ch;
    }

    List<String> res;
    public List<String> findWords3(char[][] board, String[] words) {
        // 639ms
        res = new ArrayList<>();

        int m = board.length;
        if (m < 1)
            return res;

        int n = board[0].length;

        Boolean[][] check = new Boolean[board.length][];
        for (int idx1 = 0; idx1 < check.length; idx1++) {
            check[idx1] = new Boolean[board[idx1].length];
            for (int idx2 = 0; idx2 < check[idx1].length; idx2++) {
                check[idx1][idx2] = false;
            }
        }

        for (String word : words) {
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (!res.contains(word))
                        dfs3(board, check, m, n, i, j, word, 0);
                }
            }
        }

        return res;
    }

    private void dfs3(char[][] board, Boolean[][] check, int m, int n, int i, int j, String word, int pos) {
        if (i < 0 || j < 0 || i > m - 1 || j > n - 1)
            return;

        if (check[i][j])
            return;
        
        if (board[i][j] != word.charAt(pos)) {
            return;
        }

        if (pos == word.length() - 1) {
            if (!res.contains(word))
                res.add(word);
            return;
        }

        check[i][j] = true;
        dfs3(board, check, m, n, i - 1, j, word, pos + 1);
        dfs3(board, check, m, n, i + 1, j, word, pos + 1);
        dfs3(board, check, m, n, i, j - 1, word, pos + 1);
        dfs3(board, check, m, n, i, j + 1, word, pos + 1);
        check[i][j] = false;
    }

    private void printBoard(char[][] board) {
        System.out.println("board = [");
        for (int i = 0; i < board.length; i++) {
            if (i == 0)
                System.out.println("  [" + new String(board[i]) + "]");
            else
                System.out.println(", [" + new String(board[i]) + "]");
        }
        System.out.println("]");
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").trim().split("\\]\\],\\[");
        String[] str_board = flds[0].replace("[[[", "").split("\\],\\[");

        char[][] board = new char[str_board.length][];
        for (int i = 0; i < str_board.length; i++) {
            board[i] = str_board[i].replace(",", "").toCharArray();
        }
        printBoard(board);

        Mylib ml = new Mylib();
        String[] words = ml.stringToStringArray(flds[1].replace("]]", ""));
        System.out.println("words = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        List<String> result = findWords(board, words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

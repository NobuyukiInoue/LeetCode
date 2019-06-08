import java.util.*;

public class Solution {
    public String longestWord2(String[] words) {
        Arrays.sort(words);

        Set<String> words_map = new HashSet<String>();
        String longest_word = "";
        for (String word : words) {
            if (word.length() == 1 || words_map.contains(word.substring(0, word.length() - 1))){
                if (word.length() > longest_word.length()) {
                    longest_word = word;
                }
                words_map.add(word);
            }
        }

        return longest_word;
    }

    public String longestWord(String[] words) {
        TrieNode root = new TrieNode();
        root.word = "-";
        for (String word : words)
            root.insert (word);
        return dfs(root, "");
    }

    String dfs (TrieNode node, String accum) {
        if (node == null || node.word.length() == 0)
            return accum;
        String res = "";
        if (!node.word.equals ("-"))
            accum = node.word;
        for (TrieNode child : node.links) {
            String curRes = dfs (child, accum);
            if (curRes.length() > res.length() || (curRes.length() == res.length() && curRes.compareTo(res) < 0))
                res = curRes;
        }
        return res;
    }

    /* Hand write this class every time you need to so you can remember well */
    static class TrieNode {
        String word = "";
        TrieNode[] links = new TrieNode[26];

        void insert (String s) {
            char[] chs = s.toCharArray ();
            TrieNode curNode = this;
            for (int i = 0; i < chs.length; i++) {
                int index = chs[i] - 'a';
                if (curNode.links[index] == null)
                    curNode.links[index] = new TrieNode ();
                curNode = curNode.links[index];
            }
            curNode.word = s;
        }
    }

    public String StringArray2String(String[] data) {
        if (data.length <= 0)
            return "";

        String resultStr;
        if (data[0].length() == 0) {
            resultStr = "null";
        } else {
            resultStr = data[0];
        }

        for (int i = 1; i < data.length; i++) {
            if (data[i].length() == 0) {
                resultStr += ", null";
            } else {
                resultStr += ", " + data[i];
            }

        }

        return resultStr;
    }

    public void Main(String temp) {
        String[] words = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        System.out.println("words = " + StringArray2String(words));

        long start = System.currentTimeMillis();
        
        String result = longestWord(words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

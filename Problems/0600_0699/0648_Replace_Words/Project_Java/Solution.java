import java.util.*;

public class Solution {
    class Trie {
        class TrieNode {
            char val;
            TrieNode[] map;
            boolean isWord;
            TrieNode(char c) {
                val = c;
                map = new TrieNode[26];
                isWord = false;
            }
        }
        TrieNode root;
        Trie() {
            root = new TrieNode(' ');
        }
        public void insert(String word) {
            TrieNode pointer = root;
            for (char c: word.toCharArray()) {
                if (pointer.map[c - 'a'] == null) {
                    pointer.map[c - 'a'] = new TrieNode(c);
                }
                pointer = pointer.map[c - 'a'];
            }
            pointer.isWord = true;
        }
        public String getRoot(String word) {
            TrieNode pointer = root;
            StringBuilder sb = new StringBuilder();
            for (char c: word.toCharArray()) {
                sb.append(c);
                pointer = pointer.map[c - 'a'];
                if (pointer == null) {
                    return word;
                }
                if (pointer.isWord) {
                    return sb.toString();
                }
            }
            return sb.toString();
        }
    }
    public String replaceWords(List<String> dict, String sentence) {
        // 7ms
        if (dict == null || dict.size() == 0 || sentence == null || sentence.length() == 0) {
            return "";
        }
        Trie tree = new Trie();
        for (String root: dict) {
            tree.insert(root);
        }
        String[] strs = sentence.split(" ");
        StringBuilder sb = new StringBuilder();
        for (String str: strs) {
            sb.append(tree.getRoot(str)).append(" ");
        }
        return sb.substring(0, sb.length() - 1).toString();
    }

    /*
    class TrieNode {
        private TrieNode[] children;
        private boolean isWord;
        private String content;
        public TrieNode() {
            children = new TrieNode[26];
            isWord = false;
        }
    }

    private TrieNode root = new TrieNode();

    private void addWord(String word) {
        TrieNode cur = root;
        for (int i = 0; i < word.length(); i++) {
            int index = word.charAt(i)-'a';
            if (cur.children[index] == null)
                cur.children[index] = new TrieNode();
            cur = cur.children[index];
        }
        cur.isWord = true;
        cur.content = word;
    }

    public String replaceWords(List<String> dict, String sentence) {
        // 16ms
        for (String word : dict) {
            addWord(word);
        }
        String[] strs = sentence.split("\\s+");
        StringBuilder sb = new StringBuilder();
        for (String s : strs) {
            TrieNode cur = root;
            boolean matched = false;
            for (int i = 0; i < s.length(); i++) {
                int index = s.charAt(i)-'a';
                if (cur.children[index] == null)
                    break;
                cur = cur.children[index];
                if (cur.isWord) {
                    matched = true;
                    break;
                }
            }
            if (sb.length() > 0)
                sb.append(" ");
            sb.append(matched ? cur.content : s);
        }
        return sb.toString();
    }
    */

    public String replaceWords2(List<String> dict, String sentence) {
        // 480ms
        String[] words = sentence.split(" ");
        Collections.sort(dict, (a, b) -> a.length() - b.length());
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < dict.size(); j++) {
                String currentWord = words[i];
                String currentRoot = dict.get(j);
                if (currentWord.length() < currentRoot.length())
                    break;
                if (currentWord.contains(currentRoot) && currentWord.substring(0, currentRoot.length()).equals(currentRoot))
                    words[i] = dict.get(j);
            }
        }
        String res = "";
        for (String word : words)
            res = res + word + " ";
        return res.substring(0, res.length() - 1);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String[] dict_str = flds[0].split(","); 
        List<String> dict = new ArrayList<>();
        for (int i = 0; i < dict_str.length; i++)
            dict.add(dict_str[i]);
        String sentence = flds[1];

        Mylib ml = new Mylib();
        System.out.println("dict = " + ml.listStringArrayToString(dict));
        System.out.println("sentence = " + sentence);

        long start = System.currentTimeMillis();

        String result = replaceWords(dict, sentence);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}

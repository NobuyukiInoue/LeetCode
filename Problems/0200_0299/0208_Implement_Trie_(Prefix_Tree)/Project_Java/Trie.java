import java.util.*;

class TrieNode {
    // Initialize your data structure here.
    public TrieNode[] children;
    public boolean isWord;
    public TrieNode() {
        children = new TrieNode[26];    
    }
}

class Trie {
    // 29ms
    private TrieNode root;
    private boolean startWith;

    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        insert(word, root, 0);
    }
    
    private void insert(String word, TrieNode root, int idx) {
        if (idx == word.length()) {
            root.isWord = true;
            return;
        }

        int index = word.charAt(idx) - 'a';

        if (root.children[index] == null) {
            root.children[index] = new TrieNode();
        }

        insert(word, root.children[index], idx + 1);         
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        return search(word, root, 0);         
    }

    public boolean search(String word, TrieNode root, int idx) {
        if (idx == word.length()) {
            startWith = true;
            return root.isWord;
        }

        int index = word.charAt(idx) - 'a';

        if (root.children[index] == null) {
            startWith = false;
            return false;
        }
            
        return  search(word,root.children[index], idx + 1);
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        search(prefix);
        return startWith;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */

import java.util.*;

class Trie_normal {
    // 439ms
    ArrayList<String> items;

    /** Initialize your data structure here. */
    public Trie_normal() {
        items = new ArrayList<String>();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        items.add(word);
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        for (String item : items) {
            if (word.equals(item)) {
                return true;
            }
        }

        return false;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        int len_prefix = prefix.length();

        if (len_prefix < 0) {
            return false;
        }

        for (String item :items) {
            if (item.length() >= len_prefix) {
                if (item.substring(0, len_prefix).equals(prefix)) {
                    return true;
                }
            }
        }

        return false;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */

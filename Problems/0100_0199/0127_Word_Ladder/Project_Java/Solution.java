import java.util.*;

public class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        // 532ms
        Queue<String> q = new LinkedList<>();
        q.offer(beginWord);
        int size, step = 1;
        String tmp, w2;

        while (q.size() != 0){
            size = q.size();
            for (int k = 0; k < size; k++) {
                tmp = q.poll();
                if (tmp.equals(endWord))
                    return step;
                for (int idx = 0; idx < wordList.size(); idx++) {
                    w2 = wordList.get(idx);
                    if (diff(tmp, w2) == 1) {
                        q.offer(w2);
                        wordList.remove(idx);
                        idx--;
                    }
                }
            }
            step++;
        }
        return 0;
    }

    int diff(String word1, String word2) {
        int count = 0;
        for (int i = 0; i < word1.length(); i++) {
            if (word1.charAt(i) != word2.charAt(i)) {
                count++;
            }
        }
        return count;
    }

    public int ladderLength_bad1(String beginWord, String endWord, List<String> wordList) {
        LinkedList<String> queue = new LinkedList<String>();
        queue.add(beginWord);
        wordList.add(endWord);
        int step = 0;
        while (!queue.isEmpty()) {
            LinkedList<String> level = new LinkedList<String>();
            step++;
            while (!queue.isEmpty()) {
                String q = queue.pollFirst();
                if (q.equals(endWord))
                    return step;
                for (int i = 0; i < beginWord.length(); i++) {
                    for (char c = 'a'; c <= 'z'; c++) {
                        String s = q.substring(0, i) + c + q.substring(i + 1, beginWord.length());
                        if (wordList.contains(s)) {
                            level.add(s);
                            wordList.remove(s);
                        }
                    }
                }
            }
            queue = level;
        }
        return 0;
    }

    public int ladderLength_bad2(String beginWord, String endWord, List<String> wordList) {
        Queue<String> queue = new LinkedList<String>();
        queue.add(beginWord);
        queue.add(null);

        Set<String> visited = new HashSet<String>();
        visited.add(beginWord);
        int level = 1;

        while (!queue.isEmpty()) {
            String str = queue.poll();
            if (str != null) {
                for (int i = 0; i < str.length(); i++) {
                    char[] chars = str.toCharArray();

                    for (char c = 'a'; c <= 'z'; c++) {
                        chars[i] = c;

                        String word = new String(chars);

                        if (word.equals(endWord))
                            return level + 1;

                        if (wordList.contains(word) && !visited.contains(word)) {
                            queue.add(word);
                            visited.add(word);
                        }
                    }
                }
            } else {
                level++;
                if (!queue.isEmpty()) { 
                    queue.add(null);
                }
            }
        }

       return 0;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        String beginWord = flds[0];
        String endWord   = flds[1];
        List<String> wordList = ml.stringArrayToListStringArray(flds[2].split(","));

        System.out.println("beginWord = " + beginWord);
        System.out.println("endWord   = " + endWord);
        System.out.println("wordList  = " + ml.listStringArrayToString(wordList));

        long start = System.currentTimeMillis();

        int result = ladderLength(beginWord, endWord, wordList);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

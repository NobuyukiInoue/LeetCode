import java.util.*;

public class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        // 412ms
        HashSet<String> words = new HashSet<>();
        HashSet<String> used = new HashSet<>();
        Queue<LinkedList<String>> q = new LinkedList<>();
        List<List<String>> result = new ArrayList<>();
        boolean found = false;
        
        for (String word:wordList)
            words.add(word);
        
        LinkedList<String> first = new LinkedList<>();
        first.add(beginWord);
        q.offer(first);
        used.add(beginWord);
        
        while (!q.isEmpty()) {
            int size = q.size();
            HashSet<String> localUsed = new HashSet<>();
            while (size>0) {
                LinkedList<String> curr = q.poll();
                char[] word = curr.getLast().toCharArray();
                for (int i = 0; i < word.length; i++) {
                    char temp = word[i];
                    for (int j = 'a'; j <= 'z'; j++) {
                        word[i] = (char)j;
                        String s = String.valueOf(word);
                        if (!used.contains(s) && words.contains(s)) {
                            LinkedList<String> list = new LinkedList<>(curr);
                            list.add(s);
                            if (s.equals(endWord)) {
                                found = true;
                                result.add(list);
                                continue;
                            }
                            localUsed.add(s);
                            q.offer(list);   
                        }
                    }
                    word[i] = temp;
                }
                size--;
            }
            for (String s:localUsed)
                used.add(s);
            
            if (found)
                break;
        }
        return result;
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

        List<List<String>> result = findLadders(beginWord, endWord, wordList);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listListStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

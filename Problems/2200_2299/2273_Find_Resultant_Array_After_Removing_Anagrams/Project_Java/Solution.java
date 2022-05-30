import java.util.*;

public class Solution {
    public List<String> removeAnagrams(String[] words) {
        // 2ms - 3ms
        List<String> result = new LinkedList<>();
        long prevHash = 0;
        for (int i = 0; i < words.length; ++i) {
            String curWord = words[i];
            long curHash = myHash(curWord);
            if (curHash == prevHash) {
                continue;
            } else {
                result.add(curWord);
                prevHash = curHash;
            }
        }
        return result;
    }
    
    long myHash(String s) {
        long h = 1;
        int[] counts = new int[26];
        for (char c : s.toCharArray()) {
            ++counts[c - 'a'];
        }
        for (int count : counts) {
            h *= 11;
            h += count;
        }
        return h;
    }

    public List<String> removeAnagrams2(String[] words) {
        // 4ms
        List<String> result = new ArrayList<>();
        result.add(words[0]);
        for (int i = 1; i < words.length; i++) {
            if (!isAnagram(result.get(result.size() - 1), words[i])) {
                result.add(words[i]);
            }
        }
        return result;
    }
    
    boolean isAnagram(String A, String B)
    {
        int[] arr = new int[26];
        for (int i = 0; i < A.length(); i++) {
            arr[A.charAt(i) - 'a']++;
        }
        for (int i = 0; i < B.length(); i++) {
            arr[B.charAt(i) - 'a']--;
        }
        for (int i = 0; i < 26; i++) {
            if (arr[i] != 0) {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String[] words = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[", "").replace("]", "").split(",");

        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        List<String> result = removeAnagrams(words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

import java.util.*;

public class Solution {
    public List<String> commonChars(String[] A) {
        // 4ms
        int[][] charCount = new int[A.length][26];
        for (int i = 0; i < A.length; i++) {
            for (char c : A[i].toCharArray()) {
                charCount[i][c - 'a']++;
            }
        }

        List<String> result = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            while (charCount[0][i] != 0) {
                char c = (char) (i + 'a');
                boolean valid = true;
                charCount[0][i]--;
                for (int j = 1; j < A.length; j++) {
                    if (charCount[j][i] == 0) {
                        valid = false;
                        break;
                    } else {
                        charCount[j][i]--;
                    }
                }
                if (!valid) {
                    break;
                } else {
                    result.add("" + c);
                }
            }
        }
        return result;
    }

    public List<String> commonChars2(String[] A) {
        // 7ms
        List<String> ans = new ArrayList<>();
        int[] count = new int[26]; 
        Arrays.fill(count, Integer.MAX_VALUE);
        for (String str : A) {
            int[] cnt = new int[26];
            for (int i = 0; i < str.length(); ++i) {
                ++cnt[str.charAt(i) - 'a'];
            }
            for (int i = 0; i < 26; ++i) {
                count[i] = Math.min(cnt[i], count[i]);
            }
        }
        for (char c = 'a'; c <= 'z'; ++c) {
            while (count[c - 'a']-- > 0) {
                ans.add("" + c);
            }
        }
        return ans;
    }

    private String string_array_to_string(String[] words)
    {
        if (words.length <= 0)
            return "";

        String resultStr = words[0];
        for (int i = 1; i < words.length; ++i)
            resultStr += "," + words[i];

        return resultStr;
    }

    private String list_to_String(List<String> list)
    {
        String outputStr = "";
        int listSize = list.size();
        for (int i = 0; i < listSize; ++i)
        {
            outputStr += Integer.toString(i + 1) + ":" + list.get(i) + "\n";
        }

        return outputStr;
    }

    public void Main(String temp) {
        String[] A = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        System.out.println("A = " + string_array_to_string(A));

        long start = System.currentTimeMillis();
        
        List<String> result = commonChars(A);

        long end = System.currentTimeMillis();

        System.out.println("result = \n" + list_to_String(result));
        System.out.println((end - start)  + "ms\n");
    }
}

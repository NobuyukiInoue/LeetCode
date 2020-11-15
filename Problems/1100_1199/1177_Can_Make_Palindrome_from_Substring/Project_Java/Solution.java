import java.util.*;

public class Solution {
    public List<Boolean> canMakePaliQueries(String s, int[][] queries) {
        // 7ms
        int sLength = s.length();
        List<Boolean> results = new ArrayList<>();
        int[] masks = new int[sLength + 1];

        int j = 0;
        int mask = 0;
        for (int i = 0 ; i < sLength; i++) {
            mask ^= (1 << (s.charAt(i) - 'a'));
            masks[++j] = mask;
        }

        for (int [] query : queries) {
            if (query[2] >= 13) {
                results.add(true);
            } else {
                results.add(Integer.bitCount(masks[query[1] + 1] ^ masks[query[0]]) /2 <= query[2]);
            }
        }

        return results;
    }

    public List<Boolean> canMakePaliQueries2(String s, int[][] queries) {
        // 61ms
        List<Boolean> ans = new ArrayList<>(); 
        int[][] cnt = new int[s.length() + 1][26];
        for (int i = 0; i < s.length(); ++i) {
            cnt[i + 1] = cnt[i].clone(); // copy previous sum.
            ++cnt[i + 1][s.charAt(i) - 'a'];
        }
        for (int[] q : queries) {
            int sum = 0; 
            for (int i = 0; i < 26; ++i) {
                sum += (cnt[q[1] + 1][i] - cnt[q[0]][i]) % 2;
            }
            ans.add(sum / 2 <= q[2]);
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").trim().split("\\],\\[\\[");

        String s = flds[0].replace("[[", "");
        System.out.println("s = " + s);

        String[] str_queries = flds[1].replace("]]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] queries = ml.stringToIntIntArray(str_queries);
        System.out.println("queries = " + ml.intIntArrayToString(queries));

        long start = System.currentTimeMillis();

        List<Boolean> result = canMakePaliQueries(s, queries);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listBooleanArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

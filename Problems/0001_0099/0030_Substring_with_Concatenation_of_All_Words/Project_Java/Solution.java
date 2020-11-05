import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> ans = new ArrayList<Integer>();

        if (s == null || words == null)
            return ans;
        if (s == "")
            return ans;
        if (words.length <= 0)
            return ans;
        if (words[0] == "")
            return ans;

        int n = s.length();
        int k = words[0].length();
        int t = words.length * k;

        HashMap<String, Integer> req = new HashMap<String, Integer>();
        for (String w : words)
        {
            if (req.get(w) != null)
                req.put(w, req.get(w) + 1);
            else
                req.put(w, 1);
        }

        int val_min;
        if (k < n - t + 1)
            val_min = k;
        else
            val_min = n - t + 1;

        for (int i = 0; i < val_min; ++i){
            sub_findSubstring(i, i, n, k, t, s, req, ans);
        }
        return ans;
    }

    private void sub_findSubstring(int l, int r, int n, int k, int t, String s, HashMap<String, Integer> req, List<Integer> ans)
    {
        HashMap<String, Integer> curr = new HashMap<String, Integer>();
        while (r + k <= n)
        {
            String w = s.substring(r, r + k);
            r += k;
            if (req.get(w) == null)
            {
                l = r;
                curr.clear();
            }
            else
            {
                if (curr.get(w) != null)
                    curr.put(w, curr.get(w) + 1);
                else
                    curr.put(w, 1);

                while (curr.get(w) > req.get(w))
                {
                    curr.put(s.substring(l, l + k), curr.get(s.substring(l, l + k)) - 1);
                    l += k;
                }
                if (r - l == t)
                    ans.add(l);
            }
        }
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0];

        Mylib ml = new Mylib();
        String[] words;
        if (flds.length >= 2) {
            words = ml.stringToStringArray(flds[1]);
        } else {
            words = ml.stringToStringArray("");
        }

        System.out.println("s = " + s);
        System.out.println("words[] = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        List<Integer> result = findSubstring(s, words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}

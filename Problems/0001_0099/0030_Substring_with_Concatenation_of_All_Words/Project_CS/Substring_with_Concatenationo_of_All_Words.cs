using System;
using System.Collections.Generic;

public class Solution
{
    //public IList<int> FindSubstring(string s, string[] words)
    public List<int> FindSubstring(string s, string[] words)
    {
        List<int> ans = new List<int>();

        if (s == null)
            return ans;
        if (s == "")
            return ans;
        if (words.Length <= 0)
            return ans;
        if (words[0] == "")
            return ans;
            
        int n = s.Length;
        int k = words[0].Length;
        int t = words.Length * k;

        Dictionary<string, int> req = new Dictionary<string, int>();
        foreach (string w in words)
        {
            if (req.ContainsKey(w))
                req[w]++;
            else
                req[w] = 1;
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

    private void sub_findSubstring(int l, int r, int n, int k, int t, string s, Dictionary<string, int> req, List<int> ans)
    {
        Dictionary<string, int> curr = new Dictionary<string, int>();
        while (r + k <= n)
        {
            string w = s.Substring(r, k);
            r += k;
            if (req.ContainsKey(w) == false)
            {
                l = r;
                curr.Clear();
            }
            else
            {
                if (curr.ContainsKey(w))
                    curr[w]++;
                else
                    curr[w] = 1;

                while (curr[w] > req[w])
                {
                    curr[s.Substring(l, k)] -= 1;
                    l += k;
                }
                if (r - l == t)
                    ans.Add(l);
            }
        }
    }

    public string output_int_array(int[] nums)
    {
        if (nums.Length <= 0)
            return "";

        string resultStr = "[" +  nums[0].ToString();
 
        for (int i = 1; i < nums.Length; ++i)
        {
            resultStr += "," + nums[i].ToString();
        }

        return resultStr + "]";
    }

    private string string_array_to_string(string[] words)
    {
        if (words.Length <= 0)
            return "";

        string resultStr = words[0];
        for (int i = 1; i < words.Length; ++i)
            resultStr += "," + words[i];

        return resultStr;
    }

    private string List_to_string(List<int> list)
    {
        if (list.Count <= 0)
            return "";

        string resultStr = list[0].ToString();
        for (int i = 1; i < list.Count; ++i)
            resultStr += "," + list[i].ToString();
        
        return resultStr;
    }

    public void Main(string args)
    {
        string[] flds = args.Replace("\"","").Replace("[[","").Replace("]]","").Trim().Split("],[", StringSplitOptions.None);
        string s = flds[0];
        string[] words = flds[1].Split(",");

        Console.WriteLine("s = " + s);
        Console.WriteLine("words[] = " + string_array_to_string(words));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        List<int> result = FindSubstring(s, words);
        Console.WriteLine("result = " + List_to_string(result));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}

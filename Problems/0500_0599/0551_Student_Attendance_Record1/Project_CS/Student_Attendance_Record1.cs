using System;

public class Solution
{
    public bool CheckRecord(string s)
    {
        return !(s.IndexOf("A") != s.LastIndexOf("A") || s.Contains("LLL"));
    }

    public string output_str_array(string[] words)
    {
        if (words.Length <= 0)
            return "";
        
        string results = words[0];
        for (int i = 1; i < words.Length; ++i)
        {
            results += ", " + words[i];
        }

        return results;
    }

    public void Main(string args)
    {
        string s = args.Replace("\"","").Replace(" ","").Replace("[","").Replace("]","").Trim();
        Console.WriteLine("s = " + s);
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result = CheckRecord(s);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}

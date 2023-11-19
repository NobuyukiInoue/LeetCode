using System;
using System.Collections;

public class Solution
{
    public string[] FindWords(string[] words)
    {
        // 137ms - 143ms
        int[] rowMap = new int[26];
        string[] rows = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        for (int i = 0; i < rows.Length; i++)
        {
            foreach (char ch in rows[i])
            {
                rowMap[ch - 'a'] = i;
            }
        }
        ArrayList result = new ArrayList();
        foreach (String word in words) {
            int row = rowMap[word.ToLower()[0] - 'a'];
            bool onSameRow = true;
            foreach (char ch in word.ToLower().ToCharArray())
            {
                if (rowMap[ch - 'a'] != row)
                {
                    onSameRow = false;
                    break;
                }
            }
            if (onSameRow)
            {
                result.Add(word);
            }
        }
        return (string[])result.ToArray(typeof(string));
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
        string[] words = args.Replace("\"","").Replace(" ","").Replace("[","").Replace("]","").Trim().Split(',');
        Console.WriteLine("words = [" + output_str_array(words) + "]");
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string[] result = FindWords(words);
        Console.WriteLine("result = [" + output_str_array(result) + "]");
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}

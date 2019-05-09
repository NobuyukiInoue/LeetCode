using System;
using System.Collections.Generic;

public class Solution
{
    private static byte[] charToRowMap = new byte[128];

    public Solution()
    {
        charToRowMap['q'] = 1;
        charToRowMap['w'] = 1;
        charToRowMap['e'] = 1;
        charToRowMap['r'] = 1;
        charToRowMap['t'] = 1;
        charToRowMap['y'] = 1;
        charToRowMap['u'] = 1;
        charToRowMap['i'] = 1;
        charToRowMap['o'] = 1;
        charToRowMap['p'] = 1;
        charToRowMap['Q'] = 1;
        charToRowMap['W'] = 1;
        charToRowMap['E'] = 1;
        charToRowMap['R'] = 1;
        charToRowMap['T'] = 1;
        charToRowMap['Y'] = 1;
        charToRowMap['U'] = 1;
        charToRowMap['I'] = 1;
        charToRowMap['O'] = 1;
        charToRowMap['P'] = 1;
        
        charToRowMap['a'] = 2;
        charToRowMap['s'] = 2;
        charToRowMap['d'] = 2;
        charToRowMap['f'] = 2;
        charToRowMap['g'] = 2;
        charToRowMap['h'] = 2;
        charToRowMap['j'] = 2;
        charToRowMap['k'] = 2;
        charToRowMap['l'] = 2;        
        charToRowMap['A'] = 2;
        charToRowMap['S'] = 2;
        charToRowMap['D'] = 2;
        charToRowMap['F'] = 2;
        charToRowMap['G'] = 2;
        charToRowMap['H'] = 2;
        charToRowMap['J'] = 2;
        charToRowMap['K'] = 2;
        charToRowMap['L'] = 2;
        
        charToRowMap['z'] = 3;
        charToRowMap['x'] = 3;
        charToRowMap['c'] = 3;
        charToRowMap['v'] = 3;
        charToRowMap['b'] = 3;
        charToRowMap['n'] = 3;
        charToRowMap['m'] = 3;
        charToRowMap['Z'] = 3;
        charToRowMap['X'] = 3;
        charToRowMap['C'] = 3;
        charToRowMap['V'] = 3;
        charToRowMap['B'] = 3;
        charToRowMap['N'] = 3;
        charToRowMap['M'] = 3;
    }

    public string[] FindWords(string[] words)
    {
        if (words.Length <= 0)
            return new string[0];

        var result = new List<string>(words.Length);
        foreach (var word in words)
        {
            var valid = true;
            var row = charToRowMap[word[0]];
            for (var i = 1; i < word.Length; i++)
            {
                if (row != charToRowMap[word[i]])
                {
                    valid = false;
                    break;
                }
            }
            if (valid)
                result.Add(word);
        }
        return result.ToArray();
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
        Console.WriteLine("words = " + output_str_array(words));
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string[] result = FindWords(words);
        Console.WriteLine("result = " + output_str_array(result));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}

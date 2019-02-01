using System;
using System.Collections.Generic;

public class Solution {
    public List<string> GenerateParenthesis(int n)
    {
        List<String> list = new List<String>();
        char[] str = new char[n*2];
        helper(n, n, str, 0, list);
        return list;
    }
    
    public void helper(int left, int right, char[] str, int i, List<String> list)
    {
        if (left<0 || right< left)
        {
            return ;
        }

        if (left == 0 && right == 0)
        {
            list.Add(new String(str));
        }
        else
        {
            str[i] = '(';
            helper(left - 1, right, str, i + 1, list);
            str[i] = ')';
            helper(left, right - 1, str, i + 1, list);
        }
    }

    private string List_to_String(List<string> list)
    {
        string outputStr = "";
        for (int i = 0; i < list.Count; ++i)
        {
            outputStr += (i + 1).ToString() + ":" + list[i] + "\n";
        }

        return outputStr;
    }

    public void Main(string args)
    {
        int n = int.Parse(args);

        Console.WriteLine("n = " + n.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        List<string> result = GenerateParenthesis(n);

        Console.WriteLine("Count = " + result.Count);
        Console.WriteLine("result = \n" + List_to_String(result));

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}

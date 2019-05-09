using System;
using System.Collections.Generic;

public class Solution
{
    public List<string> FullJustify(string[] words, int maxWidth)
    {
        List<string> result = new List<string>();
        int end = 0;

        while (end < words.Length)
        {
            int sum = 0;
            int start = end;

            while (end < words.Length && sum + words[end].Length <= maxWidth)
            {
                sum += words[end].Length + 1;
                end++;
            }

            string newString = "";
            if (end >= words.Length)
            {
                for (int i = start; i < end - 1; i++)
                {
                    newString += words[i] + " ";
                }

                newString += words[end - 1];
                int count = maxWidth - newString.Length;
                
                for(int j = 0; j < count; j++)
                {
                    newString += " ";
                }

                result.Add(newString);
                continue;
            }

            int spaces = maxWidth - sum;
            spaces += end - start;
            int noOfGaps = end - start - 1;

            if (noOfGaps == 0)
            {
                newString += words[end - 1];
                
                for(int j = 0; j < maxWidth - words[end - 1].Length; j++)
                {
                    newString += " ";
                }

                result.Add(newString);
                continue;
            }

            int spaceBetweenWords = spaces / noOfGaps;
            int extraSpaces = spaces % noOfGaps;

            for (int i = start; i < end - 1; i++)
            {
                newString += words[i];

                for (int j = 0; j < spaceBetweenWords; j++)
                {
                    newString += " ";
                }

                if(extraSpaces > 0)
                {
                    newString += " ";
                    extraSpaces--;
                }
            }

            newString += words[end - 1];
            result.Add(newString);
        }

        return result;
    }

    public string StringArray2String(string[] words)
    {
        if (words.Length <= 0)
            return "";

        string resultStr = "[" +  words[0].ToString();
 
        for (int i = 1; i < words.Length; ++i)
        {
            resultStr += "," + words[i].ToString();
        }

        return resultStr + "]";
    }

    public string ListArray2String(List<string> words)
    {
        if (words.Count <= 0)
            return "";

        string resultStr = "[" +  words[0].ToString();
 
        for (int i = 1; i < words.Count; ++i)
        {
            resultStr += "," + words[i].ToString();
        }

        return resultStr + "]";
    }

    public void Main(string args)
    {
        string arg_str = args.Replace("[[","").Replace("]]","").Replace("\"","").Trim();
        string[] flds = arg_str.Split(new string[] {"],["}, StringSplitOptions.None);
        string[] words = flds[0].Split(',');
        int maxWidth = int.Parse(flds[1]);

        Console.WriteLine("words[] = " + StringArray2String(words) + ", maxWidth = " + maxWidth.ToString());
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        List<string>result = FullJustify(words, maxWidth);
        
        sw.Stop();
        Console.WriteLine("result = " + ListArray2String(result));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}

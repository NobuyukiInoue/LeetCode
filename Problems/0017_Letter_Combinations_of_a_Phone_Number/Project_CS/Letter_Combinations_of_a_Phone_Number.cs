using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public IList<string> LetterCombinations(string digits)
    {
        var result = new List<string>();

        if (digits == null || digits.Length == 0) 
            return result;
        
        Dictionary<char, List<char>> my_dic = new Dictionary<char, List<char>>();
        my_dic.Add('2', new List<char> { 'a', 'b', 'c'});
        my_dic.Add('3', new List<char> { 'd', 'e', 'f'});
        my_dic.Add('4', new List<char> { 'g', 'h', 'i'});
        my_dic.Add('5', new List<char> { 'j', 'k', 'l'});
        my_dic.Add('6', new List<char> { 'm', 'n', 'o'});
        my_dic.Add('7', new List<char> { 'p', 'q', 'r', 's'});
        my_dic.Add('8', new List<char> { 't', 'u', 'v'});
        my_dic.Add('9', new List<char> { 'w', 'x', 'y', 'z'});

        result.Add("");

        foreach(var d in digits){
            var new_result = new List<string>();
            var alphabates = my_dic[d];
            
            foreach(var r in result){
                foreach(var c in alphabates){
                    new_result.Add(r + c);
                }
            }
            
            result = new_result;
        }
        
        return result;
    }

    public string output_IList(IList<string> list)
    {
        if (list.Count <= 0)
            return "";

        string resultStr = "\"" + list[0] + "\"";
        for (int i = 0; i < list.Count; ++i)
            resultStr += ", \"" + list[i] + "\"";
        
        return resultStr;
    }

    public void Main(string args)
    {
        string digits = args.Replace("\"","").Replace("[","").Replace("]","").Trim();

        Console.WriteLine("digits = " + digits);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        IList<string> result = LetterCombinations(digits);
        Console.WriteLine("result = " + output_IList(result));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}

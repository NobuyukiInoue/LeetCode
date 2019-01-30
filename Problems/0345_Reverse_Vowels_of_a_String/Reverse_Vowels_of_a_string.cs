using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Solution
{

    public string ReverseVowels(string s)
    {       
        string vowels = "AaeEoOuUiI";
        
        Stack<char> st = new Stack<char>();
        
        // Push every vowel in the string into the Stack
        for(int i = 0; i < s.Length;i++){
            
            if(vowels.IndexOf(s[i]) != -1)
                st.Push(s[i]);
        }
        
        StringBuilder result = new StringBuilder();
        // replace the vowels in the string with the stack values
        for(int i = 0; i < s.Length;i++){
            
            if(vowels.IndexOf(s[i]) != -1)
                result.Append(st.Pop());
            else
                result.Append(s[i]);
        }
        
        return result.ToString();
    }

    public string ReverseVowels_work(string s)
    {
        char[] resultStr = s.ToCharArray();
        char[] targets = new char[] {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int i = 0, j = s.Length - 1;

        while (i < j)
        {
            if (isTarget_in_Str(resultStr[i], targets)) {
                if (isTarget_in_Str(resultStr[j], targets)) {
                    resultStr[i] = s[j];
                    resultStr[j] = s[i];
                    ++i;
                }
                --j;
                continue;
            }
            ++i;
        }

        // return targets.ToString();
        string t = "";
        for (i = 0; i < resultStr.Length; ++i)
            t += resultStr[i];
        return t;
    }

    public bool isTarget_in_Str(char s, char[] targets)
    {
        for (int i = 0; i < targets.Length; ++i)
            if (s == targets[i])
                return true;
        return false;
    }

    public void Main(string args)
    {
        string var_str = args.Replace("\"","");

        Console.WriteLine("s = " + var_str);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string result = ReverseVowels(var_str);

        Console.WriteLine("result = " + result);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}

using System;

public class Solution
{
    public string LongestPalindrome(string s)
    {        
        if (string.IsNullOrEmpty(s))
        {
            return string.Empty;
        }
  
        int start = 0, end = 0;
        string result = string.Empty;
        while(end < s.Length)
        {
            if (IsPalindrome(s, start, end))
            {                
                result = (result.Length < (end - start + 1))? s.Substring(start, end - start + 1) : result;
                if (start > 0)
                    start--;
                end++;
            }
            else
            {
                start++;
            }            
        }
        return result;
    }
    
    private bool IsPalindrome(string s, int start, int end)
    {
        while(start < end){
            if (s[start] != s[end])
            {
                break;
            }
            start++;
            end--;
        }
        return !(start < end);
    }

    public void Main(string args)
    {
        string s = args.Replace("\"","").Replace("[","").Replace("]","").Trim();

        Console.WriteLine("s = " + s);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string result = LongestPalindrome(s);
        Console.WriteLine("result = " + result);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}

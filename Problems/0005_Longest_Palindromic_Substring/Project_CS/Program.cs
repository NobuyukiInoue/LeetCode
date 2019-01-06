using System;
using System.IO;

namespace Project_CS
{
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
            Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
           if (args.Length < 1)
            {
                Console.WriteLine("Usage: dotnet run Program <testdata.txt>");
                return;
            }

            if (System.IO.File.Exists(args[0]) == false)
            {
                Console.WriteLine(args[0] + "not found.");
                return;
            }

            Solution sl = new Solution();
            StreamReader sr = new StreamReader(args[0]);
            string line;

            while ((line = sr.ReadLine()) != null)
            {
                sl.Main(line);
            }

            sr.Close();
            sl = null;
        }
    }
}

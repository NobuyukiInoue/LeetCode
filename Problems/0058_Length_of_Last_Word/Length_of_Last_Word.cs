using System;

public class Solution
{
    public int LengthOfLastWord(string s)
    {
        string[] words = s.Split(' ');

        for (int i = words.Length - 1; i >= 0; --i ) {
        //    Console.WriteLine("words[" + i.ToString() + "] = " + words[i] );
            if (words[i].Length != 0) {
                return words[i].Length;
            }
        }
        
        return words[0].Length;
    }

    public void Main(string args)
    {
        Console.WriteLine("args = \"" + args + "\"");

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();

        sw.Start();

        Console.WriteLine("return = " + LengthOfLastWord( args ).ToString() );

        sw.Stop();

        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}

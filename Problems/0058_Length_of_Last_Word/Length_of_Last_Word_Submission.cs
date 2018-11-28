using System;

public class Solution
{
    public int LengthOfLastWord(string s)
    {
        if (s.Length == 0) {
            return 0;
        }

        string[] words = new string[s.Length];
        int[] space_pos = new int[s.Length];

        int i = 0, space_counts = 0;
        for ( ; i < s.Length; ++i) {
            if (s[i] == ' ')
                space_pos[space_counts++] = i;
        }
        
        if ( space_counts < space_pos.Length )
            space_pos[space_counts] = s.Length;

        if (space_counts == 0) {
            words[0] = s;
        }
        else {
            for (i = 0; i <= space_counts && i < words.Length; ++i) {
                if (space_pos[i] == 0) {
                    words[i] = "";
                }
                else {
                    if ( i == 0 )
                        words[i] = s.Substring(0, space_pos[i]);
                    else {
                        words[i] = s.Substring(space_pos[i - 1] + 1, space_pos[i] - space_pos[i - 1] - 1);
                    }
                }
            }
        }

    //    output(words, space_pos, space_counts);

        if ( space_counts == s.Length )
            i = s.Length - 1;
        else
            i = space_counts;

        for (; i >= 0; --i) {
            if (words[i].Length != 0) {
                return words[i].Length;
            }
        }
        
        return words[0].Length;
    }
    
    private void output(string[] words, int[] space_pos, int space_counts)
    {
        int i;
        
        Console.WriteLine("s.Length = " + words.Length.ToString() );
        Console.WriteLine("space_counts = " + space_counts.ToString() );
        
        for (i = 0; i < words.Length; i++) {
            Console.WriteLine("words[" + i.ToString() + "] = \"" + words[i] +"\"");
        }

        for (i = 0; i < space_pos.Length; i++) {
            Console.WriteLine("space_pos[" + i.ToString() + "] = " + space_pos[i] );
        }

        Console.WriteLine();
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

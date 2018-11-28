using System;

public class Solution
{
    public string CountAndSay(int n)
    {
        if ( n < 1 && n > 30) {
            return "";
        }

        string[] data = new string[n];
        data[0] = "1";

        int i, pos, count;

        for ( i = 1; i < n; i++ ) {
            data[i] = "";
            for ( pos = 0; pos < data[i - 1].Length; pos += count ) {
                count = count_continuity_num(data[i - 1], pos);
                data[i] += count.ToString() + data[i - 1][pos];
            }
        }
        
        return ( data[n - 1] );
    }
    
    private int count_continuity_num(string data, int pos)
    {
        int i = 0, count = 0;
        
        for ( ; (pos + i) < data.Length; ++i ) {
            if ( data[pos + i] == data[pos] ) {
                count++;
            }
            else {
                return count;
            }
        }
        
        return count;
    }

    public void Main()
    {
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();

        sw.Start();
        Console.WriteLine( CountAndSay(30) );
        sw.Stop();

        Console.WriteLine(sw.ElapsedMilliseconds.ToString() + "ƒ~ƒŠ•b");
    }
}

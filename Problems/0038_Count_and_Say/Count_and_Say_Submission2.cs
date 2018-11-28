using System;

public class Solution
{
    public string CountAndSay(int n)
    {
        if ( n < 1 && n > 30) {
            return "";
        }

        string[] data = new string[30];
        data[0] = "1";

        int i, pos, j, count;

        for ( i = 1; i < n; i++ ) {
            data[i] = "";
            pos = 0;

            while ( pos < data[i - 1].Length ) {
                count = 0;

                for ( j = 0; (pos + j) < data[i - 1].Length; ++j ) {
                    if ( data[i - 1][pos + j] == data[i - 1][pos] ) {
                        count++;
                    }
                    else {
                        break;
                    }
                }

                
                data[i] += count.ToString() + data[i - 1][pos];
                pos += count;
            }
        }
        
        return ( data[n - 1] );
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

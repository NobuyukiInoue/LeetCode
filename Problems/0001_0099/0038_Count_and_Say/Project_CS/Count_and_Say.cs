using System;

public class Solution
{
    public string CountAndSay(int n)
    {
        if ( n < 1 && n > 30)
        {
            return "";
        }

        string[] data = new string[n];

        data[0] = "1";
/*      data[1] = "11";
        data[2] = "21";
        data[3] = "1211";
        data[4] = "111221";
        data[5] = "312211";
        data[6] = "13112221";
        data[7] = "1131213211";
*/

        int i, pos, count;

        for ( i = 1; i < n; i++ )
        {
            data[i] = "";
            for ( pos = 0; pos < data[i - 1].Length; pos += count )
            {
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

    public void Main(string args)
    {
        string fld = args.Replace("[","").Replace("]","").Trim();
        int n = int.Parse(fld);

        Console.WriteLine("n = " + n);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string result = CountAndSay(n);
        Console.WriteLine("result = " + result);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}

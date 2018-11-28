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
/*        data[1] = "11";
        data[2] = "21";
        data[3] = "1211";
        data[4] = "111221";
        data[5] = "312211";
        data[6] = "13112221";
        data[7] = "1131213211";
*/

        int i, pos, count;
    //    Console.WriteLine("data[0] = " + data[0]);

        for ( i = 1; i < n; i++ ) {
            data[i] = "";
            pos = 0;

            while ( pos < data[i - 1].Length ) {
            //    Console.Write("pos = " + pos.ToString() );
            //    Console.Write(", target = " + data[i - 1].Substring( pos ));

            //    count = count_continuity_num(data[i - 1].Substring( pos ));
                count = count_continuity_num(data[i - 1], pos);

            //    Console.Write(", count = " + count.ToString() + "; ");

                data[i] += count.ToString() + data[i - 1][pos];
                pos += count;
            }

        //    Console.WriteLine("data[" + i.ToString() + "] = " + data[i]);
        //    Console.ReadLine();
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
        Console.Write( CountAndSay(30) );
    }
}

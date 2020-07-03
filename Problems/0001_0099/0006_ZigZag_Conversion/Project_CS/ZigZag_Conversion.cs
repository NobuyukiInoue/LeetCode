using System;
using System.Text;

public class Solution {
    public string Convert(string s, int numRows)
    {
        if(numRows <= 1)
            return s;

        var sb = new StringBuilder(s.Length); 
        int lap = numRows * 2 - 2;
        for (int r = 0; r < numRows && r < s.Length; r++) {
            sb.Append(s[r]);

            int d = r == 0 || r == numRows - 1 ? lap * 2 : lap;
            int m = r == numRows - 1 ? lap * 2 : lap;
            int c = r;

            while(true) {
                c = m - c;
                m += d;
                if(c >= s.Length)
                    break;
                sb.Append(s[c]);
            }
        }

        return sb.ToString();
    }

    public void Main(string args)
    {
        string[] arg_str = args.Replace("\"","").Replace("[","").Replace("]","").Trim().Split(',');
        string s = arg_str[0];
        int numRows = int.Parse(arg_str[1]);

        Console.WriteLine("s = " + s + ", numRows = " + numRows.ToString());
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string result = Convert(s, numRows);
        Console.WriteLine("result = " + result);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}

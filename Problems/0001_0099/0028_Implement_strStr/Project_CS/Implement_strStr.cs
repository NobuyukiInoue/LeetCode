using System;

public class Solution {
    public int StrStr_2(string haystack, string needle)
    {
        if ( needle == null || needle == "" )
        {
            return 0;
        }
    
        return(haystack.IndexOf(needle));
    }

    public int StrStr(string haystack, string needle)
    {
        if (needle.Length == 0) {
            return 0;
        }

        if (haystack.Length == 0) {
            return -1;
        }

        int i, j, n;
        
        for ( i = 0 ; i < haystack.Length; i++ ) {
            for ( n = i, j = 0; j < needle.Length; j++, n++ ) {
                if ( n >= haystack.Length ) {
                    return -1;
                }

                if ( haystack[n] != needle[j] ) {
                    break;
                }
            }
            
            // Console.WriteLine("i = " + i.ToString() + ", j = " + j.ToString() );

            if ( j == needle.Length ) {
                return i;
            }
        }
    
        return -1;
    }

    public void Main(string args)
    {
        string[] flds = args.Replace("\"","").Replace("[[","").Replace("]]","").Trim().Split(new string[] {"],["}, StringSplitOptions.None);
        string haystack = flds[0];
        string needle = flds[1];

        Console.WriteLine("haystack = " + haystack + "\n" + "needle = " + needle + "\n");

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = StrStr(haystack, needle);
        Console.WriteLine("result = " + result.ToString());

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}

using System;

public class Solution
{
    public string LicenseKeyFormatting(string S, int K)
    {
        var strBldr = new System.Text.StringBuilder();
        var strNoDash = S.Replace("-","").ToUpper();
        var rem = strNoDash.Length % K;
        var firstChunkCnt = rem == 0 ? K : rem;
        var remChunkCnt = (strNoDash.Length - firstChunkCnt) / K;
        
        //insanity check
        if (strNoDash.Length == 0 || firstChunkCnt <= 0){
            return "";
        }
        
        strBldr.Append(strNoDash.Substring(0,firstChunkCnt));
        for (var i = 0; i < remChunkCnt; i++){
            strBldr.Append('-');
            strBldr.Append(strNoDash.Substring(firstChunkCnt + (i * K), K));
        }
        return strBldr.ToString();    
    }

    public string LicenseKeyFormatting2(string S, int K)
    {
        char[] chars = S.ToCharArray();
        int n1 = chars.Length, n2 = 2*n1;
        char[] result = new char[n2];
        int idx2 = n2 - 1, idx1 = n1 - 1, counter = K;
        char c;

        for( ;idx1 > -1; )
        {
            c = chars[idx1--];
            if(c == '-')
            	continue;
            if (counter == 0)
            {
                result[idx2--] = '-';
                counter = K;
            }
            
            if(c >= 'a')
            {
                c -= (char)32;
            }
            result[idx2--]=c;
            counter--;
        }

        string workStr = new string(result);
        return workStr.Substring(idx2 + 1, n2 - (idx2 + 1)); 
    }

    public void Main(string args)
    {
        string arg_str = args.Replace("[[","").Replace("]]","").Trim();
        string[] flds = arg_str.Split(new string[] {"],["}, StringSplitOptions.None);
        string S = flds[0];
        int K = int.Parse(flds[1]);

        Console.WriteLine("S = " + S + ", K = " + K.ToString());
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string result = LicenseKeyFormatting(S, K);
        Console.WriteLine("result = " + result);
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}

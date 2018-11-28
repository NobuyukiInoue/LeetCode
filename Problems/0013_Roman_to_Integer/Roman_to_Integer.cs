using System;

public class Solution
{
    public class Pattern {
        public string symbol;
        public int val;
        
        public Pattern(string s, int v)
        {
            symbol = s;
            val = v;
        }
    }

    public int RomanToInt(string s)
    {
        Pattern[] pattern1 = new Pattern[7];
        pattern1[0] = new Pattern("I", 1 );
        pattern1[1] = new Pattern("V", 5 );
        pattern1[2] = new Pattern("X", 10 );
        pattern1[3] = new Pattern("L", 50 );
        pattern1[4] = new Pattern("C", 100 );
        pattern1[5] = new Pattern("D", 500 );
        pattern1[6] = new Pattern("M", 1000);

        Pattern[] pattern2 = new Pattern[6];
        pattern2[0] = new Pattern("IV",  4);
        pattern2[1] = new Pattern("IX",  9 );
        pattern2[2] = new Pattern("XL",  40 );
        pattern2[3] = new Pattern("XC",  90 );
        pattern2[4] = new Pattern("CD", 400 );
        pattern2[5] = new Pattern("CM", 900 );

        int sum = 0, i = 0, j;
        bool unmatched;

        while (i < s.Length) {
            unmatched = true;

            if (i < s.Length - 1) {

                for (j = 0; j < pattern2.Length; ++j) {
                    if ( s.Substring(i, 2) == pattern2[j].symbol) {
                        Console.WriteLine("s[i] + s[i + 1] = " + s[i] + s[i + 1]);
                        sum += pattern2[j].val;
                        unmatched = false;
                        i += 2;
                        break;
                    }
                }
            }

            if (unmatched) {
                for (j = 0; j < pattern1.Length; ++j) {
                    if ( s.Substring(i, 1) == pattern1[j].symbol) {
                        Console.WriteLine("s[i] = " + s[i]);
                        sum += pattern1[j].val;
                        i++;
                        break;
                    }
                }
            }
        }
        
        return sum;
    }

    public int RomanToInt_old(string s)
    {
        int sum = 0;

        for (int i = 0; i < s.Length ; ++i) {
            if (i == 0) {
                if (s[i] == 'I')
                    sum++;
                else if (s[i] == 'V')
                    sum += 5;
                else if (s[i] == 'X')
                    sum += 10;
                else if (s[i] == 'L')
                    sum += 50;
                else if (s[i] == 'C')
                    sum += 100;
                else if (s[i] == 'D')
                    sum += 500;
                else if (s[i] == 'M')
                    sum += 1000;
            }
            else {
                if (s[i] == 'I')
                    sum++;
                else if (s[i] == 'V' && s[i - 1] == 'I')
                    sum += 3;
                else if (s[i] == 'V')
                    sum += 5;
                else if (s[i] == 'X' && s[i - 1] == 'I')
                    sum += 8;
                else if (s[i] == 'X')
                    sum += 10;
                else if (s[i] == 'L' && s[i - 1] == 'X')
                    sum += 30;
                else if (s[i] == 'L')
                    sum += 50;
                else if (s[i] == 'C' && s[i - 1] == 'X')
                    sum += 80;
                else if (s[i] == 'C')
                    sum += 100;
                else if (s[i] == 'D' && s[i - 1] == 'C')
                    sum += 300;
                else if (s[i] == 'D')
                    sum += 500;
                else if (s[i] == 'M' && s[i - 1] == 'C')
                    sum += 800;
                else if (s[i] == 'M')
                    sum += 1000;
            }
        }

        return sum;
    }

    public void Main(string args)
    {
    //    Console.WriteLine("args = " + args);
        
        string s = args.Replace("\"", "");
        Console.WriteLine("s = " + s);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        Console.WriteLine("Result = " + RomanToInt(s).ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}

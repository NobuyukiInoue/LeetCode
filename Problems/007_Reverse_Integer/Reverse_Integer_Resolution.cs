using System;

public class Solution {
    static void Main()
    {
        //Console.WriteLine(Reverse(-123));
        Console.WriteLine(Reverse(1534236469));
    }

    /*
    static public int Reverse(int x) {
        string temp = "";
        int val = Math.Abs(x);

        if (val < 0)
            temp = "-";

        do {
            temp += (val % 10).ToString();
            val = val / 10;
        } while ( val > 0);
        
        return int.Parse(temp);
    }
    */
    static public int Reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > int.MaxValue/10 || (rev == int.MaxValue / 10 && pop > 7)) return 0;
            if (rev < int.MinValue/10 || (rev == int.MinValue / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
}


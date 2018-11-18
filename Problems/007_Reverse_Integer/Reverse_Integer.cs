using System;

public class Solution {
    static void Main()
    {
        //Console.WriteLine(Reverse(-123));
        Console.WriteLine(Reverse(1534236469));
    }

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
}


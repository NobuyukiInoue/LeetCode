using System;

public class Solution {
    public bool IsPalindrome(int x) {
        string temp = x.ToString();
        
        for (int i = 0; i < temp.Length / 2; i++) {
            if (temp[i] != temp[temp.Length - 1 - i])
                return false;
        }
        
        return true;
    }

    public void Main(string args)
    {
        int x = int.Parse(args);

        Console.WriteLine("x = " + x.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        bool result = IsPalindrome(x);

        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}

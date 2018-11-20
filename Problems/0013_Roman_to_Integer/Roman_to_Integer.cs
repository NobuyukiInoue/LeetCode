using System;

public class Solution {
    public int RomanToInt(string s)
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
	//	Console.WriteLine("args = " + args);
		
		string s = args.Replace("\"", "");
		Console.WriteLine("s = " + s);

		System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
		sw.Start();

		Console.WriteLine("Result = " + RomanToInt(s).ToString());
		
		sw.Stop();
		Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
	}
}

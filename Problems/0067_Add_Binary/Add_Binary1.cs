using System;
using System.Text;

public class Solution
{
	public string AddBinary(string a, string b)
	{
		return(Convert.ToString(ToDecimal(a) + ToDecimal(b), 2));
	}
	
	private long ToDecimal(string workStr)
	{
		long val = 0, n = 1;
		
		for (int i = workStr.Length - 1; i >= 0; --i) {
			val += (workStr[i] - '0')*n;
			n *= 2;
		}
		
	//	Console.WriteLine("val = " + val.ToString() );
		return (val);
	}

	private void output_Str(string[] data)
	{
		for (int i = 0; i < data.Length; i++) {
			Console.Write( " " + data[i] );
		}

		Console.WriteLine();
	}
	
	public void Main(string args)
	{
		Console.WriteLine("args = \"" + args + "\"");

		string[] data = args.Split(',');
		output_Str( data );

		System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();

		sw.Start();

		string str = AddBinary(data[0], data[1]);
		Console.WriteLine("Result(2) = " + str + ", Result(10) = " + ToDecimal(str) );
		
		sw.Stop();

		Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
	}
}

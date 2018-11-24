using System;

// Definition for a point.
public class Point {
	public int x;
	public int y;
	public Point() { x = 0; y = 0; }
	public Point(int a, int b) { x = a; y = b; }
 }
 
public class Solution {
	public class Propet
	{
		public double slople;
		public int first_index_num;
		public bool slople_checked;

		public Propet()
		{
			slople = 0.0;
			first_index_num = -1;
			slople_checked = false;
		}
	};

    public int MaxPoints(Point[] points)
	{
		Propet[] pt = new Propet[points.Length];
		int i, j;
		for (i = 0; i < points.Length; i++) {
			pt[i] = new Propet();
			pt[i].slople = (double)points[i].y / points[i].x;		
		}

		for (i = 0; i < points.Length; i++) {
			if (pt[i].first_index_num != -1)
				continue;
			for (j = i + 1; j < points.Length; j++) {
				if (pt[j].first_index_num != -1)
					continue;
				if (pt[i].slople == pt[j].slople) {
					pt[i].first_index_num = pt[j].first_index_num = i;
				}
			}
		}

		for (i = 0; i < points.Length; i++) {
			Console.WriteLine("pt[" + i.ToString() + "] = " + pt[i].slople.ToString());
		}

		int count = 0, max = -1, max_index = -1;
		for (i = 0; i < points.Length; i++) {
			count = 0;
			for (j = 0; j < points.Length; j++) {
				if (pt[i].first_index_num == i) {
					count++;
				}
			}

			if (count > max) {
				max = count;
				max_index = i;
			}
		}

		int max_val = -1;
		for (i = 0; i < points.Length; i++) {
			if (pt[i].first_index_num == max_index) {
				if (points[i].y > max_val) {
					max_val = points[i].y;
				}
			}
		}

		return max_val;
    }

	private Point[] set_Points(string[] flds)
	{
		Point[] p = new Point[flds.Length];

		for (int i = 0; i < flds.Length; ++i) {
			string[] temp = flds[i].Split(",");
			p[i] = new Point(int.Parse(temp[0]), int.Parse(temp[1]));
		}

		return p;
	}

	private string output_Points(Point[] p)
	{
		if (p.Length == 0)
			return "";

		string result = "[[" + p[0].x + "," + p[0].y + "]";

		for (int i = 1; i < p.Length; i++) {
			result += ",[" + p[i].x + "," + p[i].y + "]";
		}

		result += "]";

		return result;
	}

	public void Main(string args)
	{
		string temp = args.Replace("[[","").Replace("]]","");
		string[] flds = temp.Split("],[");
		Point[] p = set_Points(flds);
		Console.WriteLine("p = " + output_Points(p));

		System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
		sw.Start();

		Console.WriteLine("max = " + MaxPoints(p));
		
		sw.Stop();
		Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
	}
}

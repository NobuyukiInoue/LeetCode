using System;
using System.Collections.Generic;

// Definition for a point.
public class Point {
	public int x;
	public int y;
	public Point() { x = 0; y = 0; }
	public Point(int a, int b) { x = a; y = b; }
 }
 
public class Solution {
	public int MaxPoints(Point[] points)
	{
		return MaxPoints(points, 0, 0);
	}

	public int MaxPoints(Point[] points, int index, int maxNumberOfPoints)
	{
		if (points.Length == 0)
		{
			return 0;
		}

		if( points.Length - index <= maxNumberOfPoints)
		{
			return maxNumberOfPoints;
		}
		
		double maxKey = 0;
		int duplicatePoints = 0;

		Dictionary<double, int> slopeToCountMap = new Dictionary<double, int>();
		for (int i = index; i < points.Length; i++)
		{
			if (areEqual(points[i], points[index]))
			{
				duplicatePoints++;
			}
			else
			{
				double slope = getSlope(points[index], points[i]);
				maxKey = incrementSlopeCount(slope, slopeToCountMap, maxKey);
			}
		}

		if (slopeToCountMap.ContainsKey(maxKey))
		{
			maxNumberOfPoints = Math.Max(slopeToCountMap[maxKey] + duplicatePoints, maxNumberOfPoints);
		} else
		{
			maxNumberOfPoints = Math.Max(duplicatePoints, maxNumberOfPoints);
		}

		return MaxPoints(points, index + 1, maxNumberOfPoints);
	}

	private bool areEqual(Point a, Point b)
	{
		return a.x == b.x && a.y == b.y;
	}

	private double getSlope(Point left, Point right)
	{
		double dx = left.x - right.x;
		double dy = left.y - right.y;

		double slope = 0;
		if (dy != 0)
		{
			slope = dx / dy;
		}

		return slope;
	}

	private double incrementSlopeCount(double slope, Dictionary<double, int> slopeToCountMap, double maxKey)
	{
		if (slopeToCountMap.ContainsKey(slope))
		{
			slopeToCountMap[slope] += 1;
		}
		else
		{
			slopeToCountMap[slope] = 1;
		}

		if ((!slopeToCountMap.ContainsKey(maxKey)) || (slopeToCountMap[slope] >= slopeToCountMap[maxKey]))
		{
			maxKey = slope;
		}

		return maxKey;
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

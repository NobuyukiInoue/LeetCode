using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public int NumberOfBoomerangs(int[,] points)
    {
        int n = points.GetLength(0);
        int count = 0;

        for (int p0 = 0; p0 < n; p0++)
        {
            // Keep a lookup of the distance from p0 to all other points
            // if you find another point with same distance give that distance
            // a count of 1 (one other point), if you see another point of this
            // distance move count to 2 and so on.  
            Dictionary<int,int> distSqMap = new Dictionary<int,int>();
            for (int p1 = 0; p1 < n; p1++)
            {
                if (p1 == p0) continue;
                
                // avoid square root calculation - do distance check against distance square
                int distSq = (points[p0,0] - points[p1,0])*(points[p0,0] - points[p1,0]) 
                        + (points[p0,1] - points[p1,1])*(points[p0,1] - points[p1,1]);
                
                if (!distSqMap.ContainsKey(distSq))
                {
                    distSqMap[distSq] = 0;
                }
                else
                {
                    distSqMap[distSq]++;
                }
            }
            
            // count number of combinations for groups of equally distanced points
            foreach (int groupCount in distSqMap.Values)
            {
                count += groupCount * (groupCount + 1);
            }
        }    
        
        return count;
    }

    public int[,] str_to_int_array(string[] flds)
    {
        if (flds.Length <= 0)
            return null;

        int[,] points = new int[flds.Length, 2];
        string[] temp;

        for (int i = 0; i < flds.Length; ++i)
        {
            // Console.WriteLine("flds[" + i.ToString() + "] = " + flds[i]);
            temp = flds[i].Split(',');
            points[i,0] = int.Parse(temp[0]);
            points[i,1] = int.Parse(temp[1]);
        }

        return points;
    }

    public string output_points(int[,] points)
    {
        if (points.Length <= 0)
            return "";

        string resultStr = "[[" + points[0,0].ToString() + "," + points[0,1].ToString() + "]";
        // Console.WriteLine("points.Length = " + points.Length);

        for (int i = 1; i < points.Length / 2; ++i)
        {
            resultStr += ",[" + points[i,0].ToString() + "," + points[i,1].ToString() + "]";
            // Console.WriteLine("points[" + i.ToString() + ",0] = " + points[i,0].ToString() + "," + points[i,1].ToString());
        }

        return resultStr;
    }

    public void Main(string args)
    {
        string temp = args.Replace("[[","").Replace("]]","").Trim();
        string[] flds = temp.Split(new string[] {"],["}, StringSplitOptions.None);
        int[,] points = str_to_int_array(flds);

        Console.WriteLine("points = " + output_points(points));
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = NumberOfBoomerangs(points);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
        /*
        Console.Write("Hit Any Key");
        Console.Read();
        */
    }
}

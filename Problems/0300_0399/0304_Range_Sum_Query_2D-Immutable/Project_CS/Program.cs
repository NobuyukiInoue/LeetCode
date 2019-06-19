using System;
using System.IO;

namespace Project_CS
{
    class Program
    {
        static void Main(string[] args)
        {
           if (args.Length < 1)
            {
                Console.WriteLine("Usage: dotnet run <testdata.txt>");
                return;
            }

            if (System.IO.File.Exists(args[0]) == false)
            {
                Console.WriteLine(args[0] + " not found.");
                return;
            }

            Solution sl = new Solution();
            StreamReader sr = new StreamReader(args[0]);
            string line;

            while ((line = sr.ReadLine()) != null)
            {
                string trimmed_line = line.Trim();
                if (trimmed_line == "")
                    continue;

                sl.Main(trimmed_line);
            }

            sr.Close();
            sl = null;
        }
    }
}

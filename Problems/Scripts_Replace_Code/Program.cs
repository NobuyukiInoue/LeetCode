using System;
using System.IO;

namespace Project_CS
{
    class Program
    {
        static void Main(string[] args)
        {
            string read_FileName = "";
            string code_before_FileName = "";
            string code_after_FileName = "";
            string write_FileName = "";

            // Console.WriteLine("args.Length = " + args.Length.ToString());

            if (args.Length == 1)
            {
                Console.WriteLine("args[0] = " + args[0]);
                string[] flds = args[0].Split(' ');

                if (flds.Length != 3)
                {
                    Console.WriteLine("Usage: <target_file> <code_before_file> <code_after_file>");
                    return;
                }

                read_FileName = flds[0];
                code_before_FileName = flds[1];
                code_after_FileName = flds[2];
                write_FileName = read_FileName;
            }
            else if (args.Length < 2)
            {
                Console.WriteLine("Usage: <target_file> <code_before_file> <code_after_file>");
                return;
            }
            else if (args.Length == 3)
            {
                /*
                for (int i = 0; i < args.Length; ++i)
                {
                    Console.WriteLine("args[" + i.ToString() + "] = " + args[i]);
                }
                */

                read_FileName = args[0];
                code_before_FileName = args[1];
                code_after_FileName = args[2];
                write_FileName = read_FileName;
            }

            if (!CheckExistFile(read_FileName))
                return;
            if (!CheckExistFile(code_before_FileName))
                return;
            if (!CheckExistFile(code_after_FileName))
                return;
            if (!CheckExistFile(write_FileName))
                return;

            string readCode = File.ReadAllText(@read_FileName);
            string codeBefore = File.ReadAllText(@code_before_FileName);
            string codeAfter  = File.ReadAllText(@code_after_FileName);
            string resultCode = readCode.Replace(codeBefore, codeAfter);

            if (resultCode == readCode)
            {
            //  Console.WriteLine(@write_FileName + " was not changed.");
                return;
            }

            try
            {
                File.WriteAllText(@write_FileName, resultCode);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return;
            }

            Console.WriteLine(@write_FileName + " was changed(overwrite).");
        }

        private static bool CheckExistFile(string fileName)
        {
            if (System.IO.File.Exists(@fileName) == false)
            {
                Console.WriteLine(@fileName + " not found.");
                return false;
            }
            else
            {
                return true;
            }
        }
    }
}

# -*- coding: utf-8 -*-

import glob
import sys

def main():
    argv = sys.argv
    argc = len(argv)

    # check Arguments.
    if argc < 2:
        exit_msg(argv[0])
    target_path = argv[1]

    targetChar = "\\r\\n"
    if argc >= 3:
        argv2 = str(argv[2]).replace("\"", "")
        if argv2 == "CRLF":
           targetChar = "\\r\\n"
        elif argv2 == "CR":
           targetChar = "\\r"
        elif argv2 == "LF":
           targetChar = "\\n"

    # Get file list.
    files_list = glob.glob(target_path, recursive=True)

    count = 0
    for filename in files_list:
        f = open(filename, "rb")
        contents = f.readlines()
        f.close

        for i in range(len(contents)):
            contents_str = str(contents[i])
            if targetChar in contents_str:
                print("{0}".format(filename, targetChar))
                count += 1
                break

    print("\ntargetChar \"{0}\" was Found in {1:d} files".format(targetChar, count))

def exit_msg(argv0):
    """ print usage and exit"""
    print("Usage: python {0} <target_pattern> [targetChar]\n"
          "\n"
          "targetChar)\n"
          "    [CRLF(default) | CR | LF]\n"
          "\n"
          "example)\n"
          "python {0} \"../*/*/Project_C/*.c\" CRLF\n"
          "python {0} \"../*/*/Project_C/*.c\" LF\n"
          "python {0} \"../*/*/Project_C/lib/*.c\"\n"
          "python {0} \"../*/*/Project_C/include/*.h\"\n"
          "python {0} \"../*/*/Project_CS/*.cs\"\n"
          "python {0} \"../*/*/Project_Go/*.go\"\n"
          "python {0} \"../*/*/Project_Java/*.Java\"\n"
          "python {0} \"../*/*/Project_Python3/*.py\"\n"
          "python {0} \"../*/*/Project_Scala/*.scala\""
          .format(argv0))
    exit(0)

if __name__ == "__main__":
    main()

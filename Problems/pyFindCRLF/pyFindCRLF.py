# -*- coding: utf-8 -*-

import glob
import os
import re
import sys

def main():
    argv = sys.argv
    argc = len(argv)

    # check Arguments.
    if argc >= 2:
        targetChar = str(argv[1]).replace("\"", "")
        if targetChar != "CRLF" and targetChar != "CR" and targetChar != "LF":
            exit_msg(argv[0])
    else:
        targetChar = "CRLF"

    # Get file list.
    """
    files_list = glob.glob(target_path, recursive=True)
    """
    target_path = input("target Parrent Directory[{0}] : ".format(".."))
    if target_path == "":
        target_path = ".."

    target_file = input("target File Pattern[{0}] : ".format("*.*"))
    if target_file == "":
        target_file = "*.*"

    files_list = find_all_matched_files(target_path, target_file)

    bytesCRLF = bytes("\r\n", encoding="ascii")
    bytesLF = bytes("\n", encoding="ascii")
    bytesCR = bytes("\r", encoding="ascii")

    count = 0
    for filename in files_list:
        f = open(filename, "rb")
        contents = f.readlines()
        f.close

        if targetChar == "CRLF":
            for i in range(len(contents)):
                if bytesCRLF in contents[i]:
                    print("{0}".format(filename))
                    count += 1
                    break

        elif targetChar == "LF":
            for i in range(len(contents)):
                if bytesLF in contents[i] and bytesCRLF not in contents[i]:
                    print("{0}".format(filename))
                    count += 1
                    break

        elif targetChar == "CR":
            for i in range(len(contents)):
                if bytesCR in contents[i] and bytesLF not in contents[i]:
                    print("{0}".format(filename))
                    count += 1
                    break

    print("\ntargetChar \"{0}\" was found in {1:d} files".format(targetChar, count))

def exit_msg(argv0):
    """ print usage and exit"""
    print("Usage: python {0} [targetChar]\n"
          "\n"
          "targetChar)\n"
          "    [CRLF(default) | CR | LF]\n"
          "\n"
          "example)\n"
          "python {0} \"CRLF\n"
          "python {0} \"LF\n"
          .format(argv0))
    exit(0)

def find_all_matched_files(directory, patternStr):
    """ 指定したdirectory以下のpatternStrにマッチするファイルのパスを列挙する"""
    pattern = patternStr.replace(".", "\.").replace("*", ".*") + "$"
    fileList = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            res = re.search(pattern, file)
            if res != None:
                fileList.append(os.path.join(root, file))
    fileList.sort()
    return fileList

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-

import glob
import os
import re
import sys

from my_modules.getch import getch

def main():
    argv = sys.argv
    argc = len(argv)

    # check Arguments.
    if argc < 3:
        exit_msg(argv[0])

    if argc >= 2:
        srcChar = str(argv[1]).replace("\"", "")
        dstChar = str(argv[2]).replace("\"", "")
        if srcChar == dstChar:
            print("srcChar and dstChar are the same.")
            exit(0)
        if srcChar != "CRLF" and srcChar != "CR" and srcChar != "LF":
            exit_msg(argv[0])
        if dstChar != "CRLF" and dstChar != "CR" and dstChar != "LF":
            exit_msg(argv[0])
    else:
        srcChar = "CRLF"


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

    count, savedCount = 0, 0
    for filename in files_list:
        f = open(filename, "rb")
        contents = f.readlines()
        f.close

        hit = False
        if srcChar == "CRLF":
            for i in range(len(contents)):
                pos = contents[i].find(bytesCRLF)
                if pos >= 0:
                    if dstChar == "LF":
                        contents[i] = contents[i][:pos] + bytesLF + contents[i][pos + 2:]
                    elif dstChar == "CR":
                        contents[i] = contents[i][:pos] + bytesCR + contents[i][pos + 2:]
                    hit = True

        elif srcChar == "LF":
            for i in range(len(contents)):
                posLF = contents[i].find(bytesLF)
                posCRLF = contents[i].find(bytesCRLF)
                if posLF >= 0 and posCRLF < 0:
                    if dstChar == "CRLF":
                        contents[i] = contents[i][:posLF] + bytesCRLF + contents[i][posLF + 1:]
                    elif dstChar == "CR":
                        contents[i] = contents[i][:posLF] + bytesCR + contents[i][posLF + 1:]
                    hit = True

        elif srcChar == "CR":
            for i in range(len(contents)):
                posCR = contents[i].find(bytesLF)
                posCRLF = contents[i].find(bytesCRLF)
                if posCR >= 0 and posCRLF < 0:
                    if dstChar == "CRLF":
                        contents[i] = contents[i][:posCR] + bytesCRLF + contents[i][posCR + 1:]
                    elif dstChar == "LF":
                        contents[i] = contents[i][:posCR] + bytesLF + contents[i][posCR + 1:]
                    hit = True

        if hit:
            print("{0}".format(filename))
            count += 1

            firstKey = ''
            while (firstKey != 'Y' and firstKey != 'N'):
                print("\n{0} overwrite? (Y/N):".format(filename), end = "")
                keyRet = ord(getch())
                firstKey = chr(keyRet).upper()

            print()
            if firstKey == 'Y':
                contents_write(filename, contents)
                print("{0} was saved.".format(filename))
                savedCount += 1

    print("\nsrcChar \"{0}\" was Found in {1:d} files".format(srcChar, count))
    print("{0:d}\" files overwrite.".format(savedCount))

def exit_msg(argv0):
    """ print usage and exit"""
    print("Usage: python {0} <srcChar> <dstChar>\n"
          "\n"
          "srcChar)\n"
          "    [CRLF | CR | LF]\n"
          "\n"
          "dstChar)\n"
          "    [CRLF | CR | LF]\n"
          "\n"
          "example)\n"
          "python {0} \"CRLF LF\n"
          "python {0} \"LF CRLF\n"
          .format(argv0))
    exit(0)

def find_all_matched_files(directory, patternStr):
    """ 指定したdirectory以下のpatternStrにマッチするファイルのパスを列挙する"""
    pattern = patternStr.replace(".", "\.").replace("*", ".*") + "$"
    fileList = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            res = re.search(pattern, file)
            if res is not None:
                fileList.append(os.path.join(root, file))
    fileList.sort()
    return fileList

def contents_write(filename, contents):
    with open(filename, 'wb') as f:
        for line in contents:
            f.write(line)

if __name__ == "__main__":
    main()

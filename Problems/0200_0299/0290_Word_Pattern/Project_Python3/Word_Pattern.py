# coding: utf-8

import os
import sys
import time
import copy

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            for j in range(i + 1, len(pattern)):
                if pattern[i] == pattern[j]:
                    if words[i] != words[j]:
                        return False

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i] == words[j]:
                    if pattern[i] != pattern[j]:
                        return False
        return True

def main():
    argv = sys.argv
    argc = len(argv)

    if argc < 2:
        print("Usage: python {0} <testdata.txt>".format(argv[0]))
        exit(0)

    if not os.path.exists(argv[1]):
        print("{0} not found...".format(argv[1]))
        exit(0)

    testDataFile = open(argv[1], "r")
    lines = testDataFile.readlines()

    for temp in lines:
        temp = temp.strip()
        if temp == "":
            continue
        print("args = {0}".format(temp))
        loop_main(temp)
    #   print("Hit Return to continue...")
    #   input()

def loop_main(temp):
    tempStr = temp.replace("\"","").rstrip()

    flds = tempStr.split(',')
    pattern = flds[0]
    var_str = flds[1]

    print("pattern = {0}, str = {1}".format(pattern, var_str))

    sl = Solution()
    time0 = time.time()

    result = sl.wordPattern(pattern, var_str)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

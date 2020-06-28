# coding: utf-8

import os
import sys
import time
import copy

class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = s.rstrip()
        if len(temp) == 0:
            return 0
        while temp.find("  ") >= 0:
            temp = temp.replace("  ", " ")
        return len(temp.strip().split(" "))

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
    s = temp.replace("\"","").rstrip()

    print("s = {0}".format(s))

    sl = Solution()
    time0 = time.time()

    result = sl.countSegments(s)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

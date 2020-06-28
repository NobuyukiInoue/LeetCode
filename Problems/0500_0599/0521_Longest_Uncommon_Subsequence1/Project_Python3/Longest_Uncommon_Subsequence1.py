# coding: utf-8

import os
import sys
import time

class Solution:
#   def findLUSlength(self, a: str, b: str) -> int:
    def findLUSlength(self, a, b):
        return -1 if a == b else max(len(a), len(b))

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
    flds = temp.replace("\"","").replace(" ","").replace("[[","").replace("]]","").rstrip().split("],[")
    a = flds[0]
    b = flds[1]
    print("a = {0}".format(a))
    print("b = {0}".format(b))

    sl = Solution()
    time0 = time.time()

    result = sl.findLUSlength(a, b)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

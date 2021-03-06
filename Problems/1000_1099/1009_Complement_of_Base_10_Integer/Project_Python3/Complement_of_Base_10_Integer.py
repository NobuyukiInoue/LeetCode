# coding: utf-8

import os
import sys
import time
import collections
from functools import reduce

class Solution:
#   def bitwiseComplement(self, N: int) -> int:
    def bitwiseComplement(self, N):
        if N == 0:
            return 1
        i = 0
        while N > pow(2, i):
            i += 1
        if N == pow(2, i):
            return N - 1
        else:
            return pow(2, i) - 1 - N

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip()

    N = int(flds)
    print("N = {0:d}".format(N))

    sl = Solution()
    time0 = time.time()

    result = sl.bitwiseComplement(N)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

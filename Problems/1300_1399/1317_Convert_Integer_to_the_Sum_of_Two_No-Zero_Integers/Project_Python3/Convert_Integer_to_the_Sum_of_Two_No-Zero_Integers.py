# coding: utf-8

import functools
import operator
import os
import sys
import time

class Solution:
#   def getNoZeroIntegers(self, n: int) -> List[int]:
    def getNoZeroIntegers(self, n):
        # 24ms
        return next([a, n-a] for a in range(n) if '0' not in f'{a}{n-a}')

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
    fld = temp.replace("[","").replace("]","").replace("\"","").replace(" ","")
    n = int(fld)
    
    print("n = {0:d}".format(n))

    sl = Solution()
    time0 = time.time()
    result = sl.getNoZeroIntegers(n)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

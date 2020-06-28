# coding: utf-8

import functools
import os
import sys
import time

class Solution:
#   def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        # 328ms
        if (1 + maxChoosableInteger) * maxChoosableInteger/2 < desiredTotal:
            return False
        cInt = (1 << (maxChoosableInteger + 1)) - 1
        @functools.lru_cache(None)

        def dp(cInt,t):
            for i in range(maxChoosableInteger,0,-1):
                if 1<<i & cInt:
                    if i>=t:
                        return True
                    
                    if not dp(cInt^1<<i, t-i):
                        return True
            return False

        return dp(cInt,desiredTotal)

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
    flds = temp.replace("[","").replace("]","").replace("\"","").replace(" ","").rstrip().split(",")

    maxChoosableInteger, desiredTotal = int(flds[0]), int(flds[1])
    print("maxChoosableInteger = {0:d}, desiredTotal = {1:d}".format(maxChoosableInteger, desiredTotal))

    sl = Solution()
    time0 = time.time()
    result = sl.canIWin(maxChoosableInteger, desiredTotal)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

# coding: utf-8

import os
import sys
import time
import math

class Solution:
#   def stoneGame(self, piles: List[int]) -> bool:
    def stoneGame2(self, piles: [int]) -> bool:
        # 48ms
        if len(piles) % 2 == 0:
            return True
        return False

    def stoneGame(self, piles: [int]) -> bool:
        # 696ms
        def pmin(i, j):
            if (i,j) in mincache: return mincache[(i,j)]
            if i == j: return 0
            mincache[(i,j)] =  min(pmax(i+1, j), pmax(i, j-1))
            return mincache[(i,j)]

        def pmax(i, j):
            if (i,j) in maxcache: return maxcache[(i,j)]
            if i == j: return piles[i]
            maxcache[(i,j)] =  max(piles[i] + pmin(i+1, j), pmin(i, j-1) + piles[j])
            return maxcache[(i,j)]

        mincache, maxcache = {}, {}
        p1 = pmax(0, len(piles)-1)
        p2 = sum(piles) - p1
        return p1 > p2

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

    piles = [int(n) for n in flds.split(",")]
    print("piles = {0}".format(piles))

    sl = Solution()

    time0 = time.time()

    result = sl.stoneGame(piles)

    time1 = time.time()

    print("result = {0}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()

# coding: utf-8

import heapq
import os
import sys
import time
from typing import List, Dict, Tuple

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 980ms
        current = []
        future = sorted(zip(capital, profits))[::-1]
        for _ in range(k):
            while future and future[-1][0] <= w:
                heapq.heappush(current, -future.pop()[1])
            if current:
                w -= heapq.heappop(current)
        return w

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
    flds = temp.replace(" ", "").replace("\"", "").replace("[[", "").replace("]]", "").rstrip().split("],[")
    
    k, w = int(flds[0]), int(flds[1])
    profits = [int(_) for _ in flds[2].split(",")]
    capital = [int(_) for _ in flds[3].split(",")]
    print("k = {0:d}, w = {1:d}, profits = {2}, capital = {3}".format(k, w, profits, capital))

    sl = Solution()
    time0 = time.time()

    result = sl.findMaximizedCapital(k, w, profits, capital)

    time1 = time.time()

    print("result = {0:d}".format(result))
    print("Execute time ... : {0:f}[s]\n".format(time1 - time0))

if __name__ == "__main__":
    main()
